-- Super Club 测试数据 SQL 脚本
-- 数据库: mtuser
-- 密码: cloudese2980@HW

-- ============================================
-- 1. 创建数据库表结构
-- ============================================

-- 用户表
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100) NOT NULL,
    avatar VARCHAR(500),
    phone VARCHAR(20),
    bio TEXT,
    company VARCHAR(200),
    position VARCHAR(100),
    membership_level ENUM('free', 'premium', 'vip') DEFAULT 'free',
    membership_expiry DATETIME,
    verified BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_membership (membership_level)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 人才表
CREATE TABLE IF NOT EXISTS talents (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    company VARCHAR(200) NOT NULL,
    location VARCHAR(100) NOT NULL,
    avatar VARCHAR(500),
    description TEXT,
    bio TEXT,
    tags JSON,
    projects_count VARCHAR(20),
    experience VARCHAR(50),
    followers VARCHAR(50),
    verified BOOLEAN DEFAULT TRUE,
    available BOOLEAN DEFAULT TRUE,
    contact_info JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_location (location),
    INDEX idx_verified (verified)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 项目表
CREATE TABLE IF NOT EXISTS projects (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    type VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    full_description TEXT,
    logo VARCHAR(500),
    cover_image VARCHAR(500),
    tags JSON,
    category VARCHAR(50) NOT NULL,
    status ENUM('active', 'recruiting', 'paused', 'completed') DEFAULT 'active',
    owner_id VARCHAR(36),
    owner_name VARCHAR(100),
    owner_company VARCHAR(200),
    views INT DEFAULT 0,
    interests INT DEFAULT 0,
    contact_info JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_category (category),
    INDEX idx_status (status),
    INDEX idx_owner (owner_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 活动表
CREATE TABLE IF NOT EXISTS events (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(300) NOT NULL,
    description TEXT NOT NULL,
    full_description TEXT,
    cover VARCHAR(500),
    date DATETIME NOT NULL,
    end_date DATETIME,
    location VARCHAR(200) NOT NULL,
    location_type ENUM('online', 'offline') DEFAULT 'offline',
    address TEXT,
    meeting_link VARCHAR(500),
    category VARCHAR(50),
    status ENUM('upcoming', 'ongoing', 'past', 'cancelled') DEFAULT 'upcoming',
    capacity INT DEFAULT 100,
    registered INT DEFAULT 0,
    tags JSON,
    price DECIMAL(10, 2) DEFAULT 0,
    organizer_name VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_date (date),
    INDEX idx_location_type (location_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 社区成员表
CREATE TABLE IF NOT EXISTS links (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    user_name VARCHAR(100) NOT NULL,
    user_avatar VARCHAR(500),
    user_company VARCHAR(200),
    user_position VARCHAR(100),
    bio TEXT,
    tags JSON,
    connections_count INT DEFAULT 0,
    posts_count INT DEFAULT 0,
    influence VARCHAR(20) DEFAULT '中',
    status VARCHAR(20) DEFAULT 'online',
    verified BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_verified (verified)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 内容表
CREATE TABLE IF NOT EXISTS content (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(300) NOT NULL,
    description TEXT,
    content LONGTEXT,
    image VARCHAR(500),
    cover_image VARCHAR(500),
    type ENUM('article', 'video', 'course', 'case') DEFAULT 'article',
    department VARCHAR(50) NOT NULL,
    author_id VARCHAR(36),
    author_name VARCHAR(100),
    author_avatar VARCHAR(500),
    tags JSON,
    views INT DEFAULT 0,
    likes INT DEFAULT 0,
    comments INT DEFAULT 0,
    favorites INT DEFAULT 0,
    reading_time INT DEFAULT 5,
    published_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_type (type),
    INDEX idx_department (department),
    INDEX idx_published (published_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- 2. 插入测试数据
-- ============================================

-- 插入人才数据
INSERT INTO talents (id, name, role, company, location, avatar, description, tags, projects_count, experience, followers, verified, available) VALUES
('talent-001', '李若彤', '增长产品负责人', '酷玩科技', '上海', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop', '连续操盘 3 款出海工具产品，成功将 DAU 从 0 提升至 50w+。擅长冷启动与数据驱动增长策略。', '["冷启动", "出海", "数据驱动"]', '12', '8年', '3.4k', TRUE, TRUE),
('talent-002', '王建国', '品牌营销专家', '星辰传媒', '北京', 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&h=200&fit=crop', '10年品牌营销经验，服务过50+知名品牌，擅长品牌定位与整合营销。', '["品牌定位", "整合营销", "创意策划"]', '50+', '10年', '5.2k', TRUE, FALSE),
('talent-003', '周乙', '品牌总监', '夜航文化', '北京', 'https://images.unsplash.com/photo-1504595403659-9088ce801e29?w=200&h=200&fit=crop', '帮助消费品牌完成从定位、视觉到内容矩阵的系统打造，擅长新品上市与营销节奏设计。', '["品牌战略", "视觉体系", "上市策划"]', '27', '10年', '5.1k', TRUE, TRUE),
('talent-004', '陈音', '组织发展顾问', '镜像咨询', '深圳', 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&h=200&fit=crop', '为 30+ 科技公司搭建组织能力模型与绩效体系，擅长高速增长阶段的组织升级。', '["OD", "绩效管理", "组织升级"]', '19', '12年', '2.7k', TRUE, TRUE),
('talent-005', '王晨', '社区运营负责人', '语雀', '杭州', 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=120&h=120&fit=crop', '负责构建百万用户社区体系，搭建内容与激励模型，推动 NPS 提升 30%。', '["社区运营", "用户增长", "内容体系"]', '8', '6年', '1.8k', TRUE, TRUE),
('talent-006', '赵芷柔', 'SaaS 商业化顾问', '独立顾问', '北京', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop', '深度服务 6 家 B 端公司，帮助构建售前演示、销售手册及续费体系，年度 ARR 提升 45%。', '["商业化", "销售体系", "B2B"]', '15', '8年', '2.3k', TRUE, TRUE);

-- 插入项目数据
INSERT INTO projects (id, name, type, description, logo, tags, category, status, owner_name, owner_company, views, interests) VALUES
('proj-001', 'Mindee', 'SaaS · 客户运营', '首创"24小时贴身情绪AI伙伴"，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。', 'https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop', '["情绪AI陪护", "智能硬件", "服务商合作"]', 'AI', 'recruiting', '张创业', 'Mindee', 1234, 56),
('proj-002', '掌乐', '硬件 · 渠道拓展', '智能钢琴陪练硬件，AI实时纠错+趣味化教学。寻求教育机构、乐器店等渠道合作伙伴。', 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=120&h=120&fit=crop', '["音乐教育", "智能硬件", "渠道合作"]', '教育', 'active', '李音乐', '掌乐科技', 892, 34),
('proj-003', 'Koogle', '应用 · 工具', '像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。', 'https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop', '["跨境营销", "数据服务", "工具分发"]', '企业服务', 'active', '王跨境', 'Koogle', 756, 28),
('proj-004', '球秀', '社区 · 运动科技', 'AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。', 'https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop', '["体育品牌", "赛事合作", "内容共创"]', '文娱', 'recruiting', '张体育', '球秀科技', 623, 45);

-- 插入活动数据
INSERT INTO events (id, title, description, cover, date, end_date, location, location_type, category, status, capacity, registered, tags, price) VALUES
('event-001', '消费品牌出海空中路演 Demo Day | 线上开放麦', '亮相你的出海消费品牌，找用户、找合作、找投资。免费报名，创始人优先。', 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=900&h=600&fit=crop', '2025-11-28 19:30:00', '2025-11-28 21:30:00', '线上', 'online', '路演', 'upcoming', 200, 87, '["出海", "消费品牌", "Demo Day"]', 0),
('event-002', 'AI 创业者闭门交流会 | 北京站', '聚焦AI创业实战经验分享，限30人深度交流。', 'https://images.unsplash.com/photo-1591115765373-5207764f72e7?w=900&h=600&fit=crop', '2025-12-05 14:00:00', '2025-12-05 18:00:00', '北京·朝阳区', 'offline', '闭门会', 'upcoming', 30, 28, '["AI", "创业", "闭门会"]', 199),
('event-003', '创始人 IP，能变现的短视频 | 空中茶话会', '系统拆解从人设打造到短视频变现流程 SOP。', 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=900&h=600&fit=crop', '2025-11-27 20:00:00', '2025-11-27 22:00:00', '线上', 'online', '茶话会', 'upcoming', 150, 92, '["短视频", "IP打造", "变现"]', 0),
('event-004', '一人公司 CEO 聚会（长沙版）', '你的"一人公司"怎么样了？', 'https://images.unsplash.com/photo-1503428593586-e225b39bddfe?w=900&h=600&fit=crop', '2025-11-22 14:00:00', '2025-11-22 17:00:00', '长沙', 'offline', '聚会', 'upcoming', 50, 35, '["一人公司", "创业者", "交流"]', 0);

-- 插入社区成员数据
INSERT INTO links (id, user_id, user_name, user_avatar, user_company, user_position, bio, tags, connections_count, posts_count, influence, status, verified) VALUES
('link-001', 'user-101', '张小美', 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop', '美丽消费', '创始人', '专注美妆个护赛道，2年内打造3个爆款产品，总GMV突破5000万。', '["消费", "美妆", "品牌运营"]', 234, 45, '高', 'online', TRUE),
('link-002', 'user-102', '李技术', 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop', '云端科技', 'CTO', '10年技术研发经验，擅长云计算和大数据架构。', '["技术", "云计算", "大数据"]', 567, 89, '高', 'offline', TRUE),
('link-003', 'user-103', '王创业', 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop', '星辰创投', '投资经理', '关注早期AI和SaaS项目，已投资20+初创公司。', '["投资", "AI", "SaaS"]', 445, 67, '高', 'online', TRUE),
('link-004', 'user-104', '刘营销', 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop', '增长工场', '营销总监', '擅长增长黑客和私域运营，帮助多家企业实现用户增长突破。', '["增长", "营销", "私域"]', 389, 102, '中', 'online', TRUE);

-- 插入内容数据
INSERT INTO content (id, title, description, image, type, department, author_name, author_avatar, tags, views, likes, comments, reading_time) VALUES
('content-001', '《别让猴子跳回背上》如何做一个合理的管理者(下)', '作为管理者,你的贡献来自于你的判断力与影响力,而非你干了多少具体的活儿。本文通过"猴子"隐喻,教你如何避免成为下属问题的承担者。', 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop', 'article', '战略部', '管理大师', 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=100&h=100&fit=crop', '["管理", "领导力", "时间管理"]', 2345, 189, 23, 8),
('content-002', '品牌定位的底层逻辑', '深入解析品牌定位的本质，从用户心智到市场竞争，构建清晰的品牌战略。', 'https://images.unsplash.com/photo-1552664730-d307ca884978?w=400&h=250&fit=crop', 'article', '品牌部', '品牌专家', 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop', '["品牌", "定位", "营销"]', 1876, 145, 18, 12),
('content-003', '《上瘾》如何培养用户的使用习惯?(下)', '成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起。', 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop', 'article', '产品部', '产品专家', 'https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=100&fit=crop', '["产品", "用户习惯", "增长"]', 3210, 267, 45, 10),
('content-004', '如何打造高效团队', '从招聘、培训到激励，全方位解析高效团队的打造方法。', 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&h=250&fit=crop', 'article', '人力部', 'HR专家', 'https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=100&h=100&fit=crop', '["团队管理", "人力资源", "组织建设"]', 1654, 132, 29, 15);

-- 创建统计视图
CREATE OR REPLACE VIEW talents_stats AS
SELECT
    COUNT(*) as totalTalents,
    COUNT(DISTINCT SUBSTRING_INDEX(description, '赛道', 1)) as totalTracks,
    (SELECT COUNT(*) FROM events WHERE status = 'upcoming') as activeInvitations
FROM talents;

-- 完成
SELECT '测试数据插入完成！' as message;
