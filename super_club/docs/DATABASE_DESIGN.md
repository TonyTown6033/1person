# Super Club 数据库设计文档

## 数据库选型

推荐使用 **PostgreSQL** 作为主数据库，原因：
- 支持复杂查询和事务
- 优秀的全文搜索功能
- JSON 字段支持
- 成熟的生态系统

## 数据表设计

### 1. 用户表 (users)

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    avatar VARCHAR(500),
    phone VARCHAR(20),
    bio TEXT,
    company VARCHAR(200),
    position VARCHAR(100),
    membership_level VARCHAR(20) DEFAULT 'free', -- free, premium, vip
    membership_expiry TIMESTAMP,
    verified BOOLEAN DEFAULT FALSE,
    email_verified BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_membership ON users(membership_level);
CREATE INDEX idx_users_created_at ON users(created_at DESC);
```

### 2. 人才表 (talents)

```sql
CREATE TABLE talents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(200) NOT NULL,
    company VARCHAR(200) NOT NULL,
    location VARCHAR(100),
    avatar VARCHAR(500),
    description TEXT,
    bio TEXT,
    tags TEXT[], -- PostgreSQL 数组类型
    verified BOOLEAN DEFAULT FALSE,
    available BOOLEAN DEFAULT TRUE,
    stats JSONB DEFAULT '{"projects": "0", "experience": "0", "followers": "0"}',
    skills JSONB DEFAULT '[]',
    education JSONB DEFAULT '[]',
    contact JSONB,
    view_count INTEGER DEFAULT 0,
    follower_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_talents_user_id ON talents(user_id);
CREATE INDEX idx_talents_location ON talents(location);
CREATE INDEX idx_talents_tags ON talents USING GIN(tags);
CREATE INDEX idx_talents_verified ON talents(verified);
CREATE INDEX idx_talents_available ON talents(available);
CREATE INDEX idx_talents_follower_count ON talents(follower_count DESC);

-- 全文搜索索引
CREATE INDEX idx_talents_search ON talents USING GIN(
    to_tsvector('chinese', name || ' ' || COALESCE(description, '') || ' ' || company)
);
```

### 3. 人才技能表 (talent_skills)

```sql
CREATE TABLE talent_skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    talent_id UUID REFERENCES talents(id) ON DELETE CASCADE,
    skill_name VARCHAR(100) NOT NULL,
    skill_level VARCHAR(20), -- beginner, intermediate, advanced, expert
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_talent_skills_talent_id ON talent_skills(talent_id);
CREATE INDEX idx_talent_skills_name ON talent_skills(skill_name);
```

### 4. 项目表 (projects)

```sql
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    owner_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    type VARCHAR(100),
    description TEXT NOT NULL,
    full_description TEXT,
    logo VARCHAR(500),
    cover_image VARCHAR(500),
    tags TEXT[],
    category VARCHAR(50),
    status VARCHAR(20) DEFAULT 'active', -- active, recruiting, paused, completed
    view_count INTEGER DEFAULT 0,
    interest_count INTEGER DEFAULT 0,
    collaboration_count INTEGER DEFAULT 0,
    contact JSONB,
    needs JSONB DEFAULT '[]',
    milestones JSONB DEFAULT '[]',
    team JSONB DEFAULT '[]',
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_projects_owner_id ON projects(owner_id);
CREATE INDEX idx_projects_category ON projects(category);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_tags ON projects USING GIN(tags);
CREATE INDEX idx_projects_featured ON projects(is_featured);
CREATE INDEX idx_projects_created_at ON projects(created_at DESC);

-- 全文搜索
CREATE INDEX idx_projects_search ON projects USING GIN(
    to_tsvector('chinese', name || ' ' || description)
);
```

### 5. 项目合作意向表 (project_interests)

```sql
CREATE TABLE project_interests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    message TEXT,
    capability TEXT,
    contact JSONB,
    status VARCHAR(20) DEFAULT 'pending', -- pending, accepted, rejected
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(project_id, user_id)
);

CREATE INDEX idx_project_interests_project_id ON project_interests(project_id);
CREATE INDEX idx_project_interests_user_id ON project_interests(user_id);
CREATE INDEX idx_project_interests_status ON project_interests(status);
```

### 6. 活动表 (events)

```sql
CREATE TABLE events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(300) NOT NULL,
    description TEXT NOT NULL,
    full_description TEXT,
    cover VARCHAR(500),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    location VARCHAR(200),
    location_type VARCHAR(20), -- online, offline
    address TEXT,
    meeting_link VARCHAR(500),
    category VARCHAR(50),
    status VARCHAR(20) DEFAULT 'upcoming', -- upcoming, ongoing, past, cancelled
    capacity INTEGER,
    registered_count INTEGER DEFAULT 0,
    price DECIMAL(10, 2) DEFAULT 0,
    requirements TEXT,
    benefits TEXT[],
    tags TEXT[],
    agenda JSONB DEFAULT '[]',
    speakers JSONB DEFAULT '[]',
    organizer JSONB,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_events_start_date ON events(start_date);
CREATE INDEX idx_events_status ON events(status);
CREATE INDEX idx_events_category ON events(category);
CREATE INDEX idx_events_featured ON events(is_featured);
CREATE INDEX idx_events_location_type ON events(location_type);
```

### 7. 活动报名表 (event_registrations)

```sql
CREATE TABLE event_registrations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id UUID REFERENCES events(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    attendee_info JSONB NOT NULL,
    note TEXT,
    questions JSONB,
    status VARCHAR(20) DEFAULT 'confirmed', -- confirmed, cancelled, attended
    qr_code VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(event_id, user_id)
);

CREATE INDEX idx_event_registrations_event_id ON event_registrations(event_id);
CREATE INDEX idx_event_registrations_user_id ON event_registrations(user_id);
CREATE INDEX idx_event_registrations_status ON event_registrations(status);
```

### 8. 社区连接表 (connections)

```sql
CREATE TABLE connections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    requester_id UUID REFERENCES users(id) ON DELETE CASCADE,
    target_id UUID REFERENCES users(id) ON DELETE CASCADE,
    message TEXT,
    purpose VARCHAR(50),
    status VARCHAR(20) DEFAULT 'pending', -- pending, connected, rejected
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(requester_id, target_id)
);

CREATE INDEX idx_connections_requester_id ON connections(requester_id);
CREATE INDEX idx_connections_target_id ON connections(target_id);
CREATE INDEX idx_connections_status ON connections(status);
```

### 9. 内容表 (contents)

```sql
CREATE TABLE contents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(300) NOT NULL,
    description TEXT,
    excerpt TEXT,
    content TEXT,
    image VARCHAR(500),
    cover_image VARCHAR(500),
    type VARCHAR(20), -- article, video, course, case
    department VARCHAR(50),
    author_id UUID REFERENCES users(id),
    tags TEXT[],
    view_count INTEGER DEFAULT 0,
    like_count INTEGER DEFAULT 0,
    comment_count INTEGER DEFAULT 0,
    favorite_count INTEGER DEFAULT 0,
    reading_time INTEGER,
    published_at TIMESTAMP,
    is_published BOOLEAN DEFAULT FALSE,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_contents_type ON contents(type);
CREATE INDEX idx_contents_department ON contents(department);
CREATE INDEX idx_contents_author_id ON contents(author_id);
CREATE INDEX idx_contents_tags ON contents USING GIN(tags);
CREATE INDEX idx_contents_published ON contents(is_published);
CREATE INDEX idx_contents_featured ON contents(is_featured);
CREATE INDEX idx_contents_published_at ON contents(published_at DESC);

-- 全文搜索
CREATE INDEX idx_contents_search ON contents USING GIN(
    to_tsvector('chinese', title || ' ' || COALESCE(description, ''))
);
```

### 10. 评论表 (comments)

```sql
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content_id UUID REFERENCES contents(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    parent_id UUID REFERENCES comments(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    like_count INTEGER DEFAULT 0,
    is_deleted BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_comments_content_id ON comments(content_id);
CREATE INDEX idx_comments_user_id ON comments(user_id);
CREATE INDEX idx_comments_parent_id ON comments(parent_id);
CREATE INDEX idx_comments_created_at ON comments(created_at DESC);
```

### 11. 收藏表 (favorites)

```sql
CREATE TABLE favorites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    resource_type VARCHAR(20) NOT NULL, -- talent, project, event, content
    resource_id UUID NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, resource_type, resource_id)
);

CREATE INDEX idx_favorites_user_id ON favorites(user_id);
CREATE INDEX idx_favorites_resource ON favorites(resource_type, resource_id);
CREATE INDEX idx_favorites_created_at ON favorites(created_at DESC);
```

### 12. 点赞表 (likes)

```sql
CREATE TABLE likes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    resource_type VARCHAR(20) NOT NULL, -- content, comment
    resource_id UUID NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, resource_type, resource_id)
);

CREATE INDEX idx_likes_user_id ON likes(user_id);
CREATE INDEX idx_likes_resource ON likes(resource_type, resource_id);
```

### 13. 邀约表 (invitations)

```sql
CREATE TABLE invitations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    talent_id UUID REFERENCES talents(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    message TEXT,
    preferred_date TIMESTAMP,
    topic VARCHAR(200),
    duration INTEGER, -- 分钟
    status VARCHAR(20) DEFAULT 'pending', -- pending, accepted, rejected, completed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_invitations_talent_id ON invitations(talent_id);
CREATE INDEX idx_invitations_user_id ON invitations(user_id);
CREATE INDEX idx_invitations_status ON invitations(status);
CREATE INDEX idx_invitations_preferred_date ON invitations(preferred_date);
```

### 14. 轮播图表 (carousels)

```sql
CREATE TABLE carousels (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    page VARCHAR(50) NOT NULL, -- events, links, home
    image VARCHAR(500) NOT NULL,
    title VARCHAR(200),
    subtitle VARCHAR(200),
    link VARCHAR(500),
    order_num INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_carousels_page ON carousels(page);
CREATE INDEX idx_carousels_order ON carousels(order_num);
CREATE INDEX idx_carousels_active ON carousels(is_active);
```

### 15. 通知表 (notifications)

```sql
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL, -- invitation, connection, event, system
    title VARCHAR(200) NOT NULL,
    content TEXT,
    link VARCHAR(500),
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_notifications_user_id ON notifications(user_id);
CREATE INDEX idx_notifications_is_read ON notifications(is_read);
CREATE INDEX idx_notifications_created_at ON notifications(created_at DESC);
```

## 视图 (Views)

### 用户统计视图

```sql
CREATE VIEW user_stats AS
SELECT
    u.id,
    u.name,
    COUNT(DISTINCT p.id) as project_count,
    COUNT(DISTINCT c.id) FILTER (WHERE c.status = 'connected') as connection_count,
    COUNT(DISTINCT er.id) as event_count,
    COUNT(DISTINCT f.id) as favorite_count
FROM users u
LEFT JOIN projects p ON p.owner_id = u.id
LEFT JOIN connections c ON c.requester_id = u.id OR c.target_id = u.id
LEFT JOIN event_registrations er ON er.user_id = u.id
LEFT JOIN favorites f ON f.user_id = u.id
GROUP BY u.id, u.name;
```

### 热门人才视图

```sql
CREATE VIEW popular_talents AS
SELECT
    t.*,
    COUNT(DISTINCT i.id) as invitation_count,
    COUNT(DISTINCT f.id) as favorite_count
FROM talents t
LEFT JOIN invitations i ON i.talent_id = t.id
LEFT JOIN favorites f ON f.resource_type = 'talent' AND f.resource_id = t.id
WHERE t.verified = TRUE AND t.available = TRUE
GROUP BY t.id
ORDER BY favorite_count DESC, invitation_count DESC
LIMIT 100;
```

## 触发器 (Triggers)

### 自动更新 updated_at

```sql
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- 应用到所有表
CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_talents_updated_at BEFORE UPDATE ON talents
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_projects_updated_at BEFORE UPDATE ON projects
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_events_updated_at BEFORE UPDATE ON events
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_contents_updated_at BEFORE UPDATE ON contents
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
```

### 自动更新计数器

```sql
-- 更新活动报名人数
CREATE OR REPLACE FUNCTION update_event_registration_count()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE events SET registered_count = registered_count + 1
        WHERE id = NEW.event_id;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE events SET registered_count = GREATEST(registered_count - 1, 0)
        WHERE id = OLD.event_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER event_registration_count_trigger
AFTER INSERT OR DELETE ON event_registrations
FOR EACH ROW EXECUTE FUNCTION update_event_registration_count();

-- 更新内容评论数
CREATE OR REPLACE FUNCTION update_content_comment_count()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE contents SET comment_count = comment_count + 1
        WHERE id = NEW.content_id;
    ELSIF TG_OP = 'DELETE' AND OLD.is_deleted = FALSE THEN
        UPDATE contents SET comment_count = GREATEST(comment_count - 1, 0)
        WHERE id = OLD.content_id;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER content_comment_count_trigger
AFTER INSERT OR DELETE OR UPDATE ON comments
FOR EACH ROW EXECUTE FUNCTION update_content_comment_count();
```

## 数据迁移脚本

### 初始化管理员用户

```sql
INSERT INTO users (email, password_hash, name, membership_level, verified)
VALUES ('admin@superclub.com', '$2b$10$...', 'Super Admin', 'vip', TRUE);
```

### 初始化分类数据

```sql
-- 插入示例轮播图
INSERT INTO carousels (page, image, title, subtitle, link, order_num) VALUES
('events', 'https://images.unsplash.com/photo-1540575467063-178a50c2df87', 'Super Club 创业者社区', '连接优秀创业者', '/events', 1),
('events', 'https://images.unsplash.com/photo-1591115765373-5207764f72e7', '每周精彩活动', '200+ 分享嘉宾', '/events', 2),
('links', 'https://images.unsplash.com/photo-1511632765486-a01980e01a18', 'Starter Network', '连接优秀创业者', '/links', 1);
```

## 性能优化建议

### 1. 分区表

对于大表可以考虑分区：

```sql
-- 按月分区事件表
CREATE TABLE events_2025_11 PARTITION OF events
FOR VALUES FROM ('2025-11-01') TO ('2025-12-01');
```

### 2. 物化视图

对于复杂统计查询：

```sql
CREATE MATERIALIZED VIEW talent_statistics AS
SELECT
    DATE_TRUNC('day', created_at) as date,
    COUNT(*) as new_talents,
    COUNT(*) FILTER (WHERE verified = TRUE) as verified_talents
FROM talents
GROUP BY DATE_TRUNC('day', created_at);

-- 定期刷新
REFRESH MATERIALIZED VIEW talent_statistics;
```

### 3. 读写分离

- 主库：处理写操作
- 从库：处理读操作

### 4. 缓存策略

使用 Redis 缓存：
- 热门数据（精选人才、热门活动）
- 用户会话信息
- 统计数据

## 备份策略

```bash
# 每日备份
pg_dump -U postgres -d superclub > backup_$(date +%Y%m%d).sql

# 恢复
psql -U postgres -d superclub < backup_20251111.sql
```

## 监控指标

- 表大小和增长趋势
- 查询性能（慢查询日志）
- 索引使用情况
- 连接数
- 缓存命中率
