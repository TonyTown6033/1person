-- 插入测试文章数据
-- 执行方式：psql -U postgres -d your_database -f insert_test_articles.sql

-- 首先创建测试用户（如果不存在）
INSERT INTO users (id, email, password_hash, name, avatar, is_active, created_at, updated_at)
VALUES (
    '00000000-0000-0000-0000-000000000001',
    'test@example.com',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyY5Y5Y5Y5Y5',  -- 密码: test123
    '测试用户',
    'https://api.dicebear.com/7.x/avataaars/svg?seed=test',
    true,
    NOW(),
    NOW()
) ON CONFLICT (email) DO NOTHING;

-- 清理旧的测试文章（可选）
DELETE FROM contents WHERE title LIKE '测试%' OR title IN (
    '如何做一个合理的管理者',
    '为什么领导没时间，下属没事做？',
    '如何培养用户的使用习惯？',
    '让产品成为用户生活中不可或缺的一部分'
);

-- 插入4篇测试文章
INSERT INTO contents (id, title, description, content, type, department, author_id, 
                      cover_image, tags, is_published, published_at, reading_time,
                      view_count, like_count, comment_count, favorite_count, created_at, updated_at)
VALUES 
(
    gen_random_uuid(),
    '如何做一个合理的管理者',
    '作为管理者，你的贡献来自于你的判断力与影响力，你的职责不是亲力亲为地背负所有猴子，而是要提供动力让其他人发挥所长。',
    'articles/article-1.md',
    'article',
    '人力部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&h=400&fit=crop',
    ARRAY['管理', '领导力', '团队'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
),
(
    gen_random_uuid(),
    '为什么领导没时间，下属没事做？',
    '一旦你接受了这些本不属于你的猴子，一个更严重的问题便随之而来：你为什么越努力，反而越忙乱？',
    'articles/article-2.md',
    'article',
    '人力部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&h=400&fit=crop',
    ARRAY['管理', '效率', '授权'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
),
(
    gen_random_uuid(),
    '如何培养用户的使用习惯？',
    '成功的习惯养成类产品，本质上是将用户面临的问题与产品提供的解决方案，通过一次又一次的循环，紧密地联系在一起。',
    'articles/article-3.md',
    'article',
    '品牌部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&h=400&fit=crop',
    ARRAY['产品', '用户习惯', '增长'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
),
(
    gen_random_uuid(),
    '让产品成为用户生活中不可或缺的一部分',
    '在这个注意力稀缺的时代，如何让你的产品成为用户生活中不可或缺的一部分？',
    'articles/article-4.md',
    'article',
    '品牌部',
    '00000000-0000-0000-0000-000000000001',
    'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=800&h=400&fit=crop',
    ARRAY['产品', '用户体验', '价值'],
    true,
    NOW(),
    5,
    0, 0, 0, 0,
    NOW(),
    NOW()
);

-- 查询插入的文章
SELECT id, title, department, content as markdown_file 
FROM contents 
WHERE title IN (
    '如何做一个合理的管理者',
    '为什么领导没时间，下属没事做？',
    '如何培养用户的使用习惯？',
    '让产品成为用户生活中不可或缺的一部分'
)
ORDER BY created_at DESC;







