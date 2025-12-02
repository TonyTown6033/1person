#!/usr/bin/env python3
"""
数据库测试数据填充脚本
为Super Club应用填充测试数据
"""
import sys
from pathlib import Path
from datetime import datetime, timedelta
from decimal import Decimal

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from app.core.database import SessionLocal
from app.models import User, Talent, Project, Event, Connection, Content, Carousel
def hash_password(password: str) -> str:
    """生成密码哈希 - 使用简单的哈希用于测试"""
    # 使用一个预先生成的bcrypt哈希 for "password123"
    # 这是 bcrypt.hashpw(b"password123", bcrypt.gensalt()) 的结果
    return "$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Lam2"

def seed_users(db):
    """创建测试用户"""
    print("创建用户数据...")

    users = [
        User(
            email="zhangsan@example.com",
            password_hash=hash_password("password123"),
            name="张三",
            avatar="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200&h=200&fit=crop",
            company="创新科技",
            position="CEO",
            membership_level="premium",
            verified=True,
            email_verified=True
        ),
        User(
            email="lisi@example.com",
            password_hash=hash_password("password123"),
            name="李四",
            avatar="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&h=200&fit=crop",
            company="星辰传媒",
            position="CTO",
            membership_level="vip",
            verified=True,
            email_verified=True
        ),
        User(
            email="wangwu@example.com",
            password_hash=hash_password("password123"),
            name="王五",
            avatar="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop",
            company="美丽消费",
            position="创始人",
            membership_level="premium",
            verified=True,
            email_verified=True
        ),
        User(
            email="zhaoliu@example.com",
            password_hash=hash_password("password123"),
            name="赵六",
            avatar="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&h=200&fit=crop",
            company="云端科技",
            position="产品经理",
            membership_level="free",
            verified=True,
            email_verified=True
        ),
    ]

    for user in users:
        db.add(user)

    db.commit()
    print(f"✓ 创建了 {len(users)} 个用户")
    return users

def seed_talents(db, users):
    """创建人才数据"""
    print("创建人才数据...")

    talents = [
        Talent(
            user_id=users[0].id,
            name="李若彤",
            role="增长产品负责人",
            company="酷玩科技",
            location="上海",
            avatar="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&h=200&fit=crop",
            description="连续操盘 3 款出海工具产品，成功将 DAU 从 0 提升至 50w+。擅长冷启动与数据驱动增长策略。",
            tags=["冷启动", "出海", "数据驱动"],
            stats={"projects": "12", "experience": "8年", "followers": "3.4k"},
            verified=True,
            available=True
        ),
        Talent(
            user_id=users[1].id,
            name="王建国",
            role="品牌营销专家",
            company="星辰传媒",
            location="北京",
            avatar="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&h=200&fit=crop",
            description="10年品牌营销经验，服务过50+知名品牌，擅长品牌定位与整合营销。",
            tags=["品牌定位", "整合营销", "创意策划"],
            stats={"projects": "50+", "experience": "10年", "followers": "5.2k"},
            verified=True,
            available=False
        ),
        Talent(
            user_id=users[2].id,
            name="周乙",
            role="品牌总监",
            company="夜航文化",
            location="北京",
            avatar="https://images.unsplash.com/photo-1504595403659-9088ce801e29?w=200&h=200&fit=crop",
            description="帮助消费品牌完成从定位、视觉到内容矩阵的系统打造，擅长新品上市与营销节奏设计。",
            tags=["品牌战略", "视觉体系", "上市策划"],
            stats={"projects": "27", "experience": "10年", "followers": "5.1k"},
            verified=True,
            available=True
        ),
        Talent(
            user_id=users[3].id,
            name="陈音",
            role="组织发展顾问",
            company="镜像咨询",
            location="深圳",
            avatar="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=200&h=200&fit=crop",
            description="为 30+ 科技公司搭建组织能力模型与绩效体系，擅长高速增长阶段的组织升级。",
            tags=["OD", "绩效管理", "组织升级"],
            stats={"projects": "19", "experience": "12年", "followers": "2.7k"},
            verified=True,
            available=True
        ),
        Talent(
            user_id=users[0].id,
            name="王晨",
            role="社区运营负责人",
            company="语雀",
            location="杭州",
            avatar="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=120&h=120&fit=crop",
            description="负责构建百万用户社区体系，搭建内容与激励模型，推动 NPS 提升 30%。",
            tags=["社区运营", "用户增长", "内容体系"],
            stats={"projects": "8", "experience": "6年", "followers": "1.8k"},
            verified=True,
            available=True
        ),
        Talent(
            user_id=users[1].id,
            name="赵芷柔",
            role="SaaS 商业化顾问",
            company="独立顾问",
            location="北京",
            avatar="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&h=120&fit=crop",
            description="深度服务 6 家 B 端公司，帮助构建售前演示、销售手册及续费体系，年度 ARR 提升 45%。",
            tags=["商业化", "销售体系", "B2B"],
            stats={"projects": "15", "experience": "8年", "followers": "2.3k"},
            verified=True,
            available=True
        ),
    ]

    for talent in talents:
        db.add(talent)

    db.commit()
    print(f"✓ 创建了 {len(talents)} 个人才")

def seed_projects(db, users):
    """创建项目数据"""
    print("创建项目数据...")

    projects = [
        Project(
            owner_id=users[0].id,
            name="Mindee",
            type="SaaS · 客户运营",
            description='首创"24小时贴身情绪AI伙伴"，陪伴一监测一干预一成长全流程守护。需要算力、服务商、线下运营咨询、医院、资质等方向的合作。',
            logo="https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=120&h=120&fit=crop",
            tags=["情绪AI陪护", "智能硬件", "服务商合作"],
            category="AI",
            status="recruiting",
            view_count=1234,
            interest_count=56
        ),
        Project(
            owner_id=users[1].id,
            name="掌乐",
            type="硬件 · 渠道拓展",
            description="智能钢琴陪练硬件，AI实时纠错+趣味化教学。寻求教育机构、乐器店等渠道合作伙伴。",
            logo="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=120&h=120&fit=crop",
            tags=["音乐教育", "智能硬件", "渠道合作"],
            category="教育",
            status="active",
            view_count=892,
            interest_count=34
        ),
        Project(
            owner_id=users[2].id,
            name="Koogle",
            type="应用 · 工具",
            description="像使用 Google 一样快速准确地检索海外头条，帮助跨境营销团队提升海外研究效率。",
            logo="https://images.unsplash.com/photo-1580894732444-8ecded7900cd?w=120&h=120&fit=crop",
            tags=["跨境营销", "数据服务", "工具分发"],
            category="企业服务",
            status="active",
            view_count=756,
            interest_count=28
        ),
        Project(
            owner_id=users[3].id,
            name="球秀",
            type="社区 · 运动科技",
            description="AI驱动的运动社区视频平台，连接教练、运动达人与品牌，为运动生态提供内容解决方案。",
            logo="https://images.unsplash.com/photo-1545239351-1141bd82e8a6?w=120&h=120&fit=crop",
            tags=["体育品牌", "赛事合作", "内容共创"],
            category="文娱",
            status="recruiting",
            view_count=623,
            interest_count=45
        ),
    ]

    for project in projects:
        db.add(project)

    db.commit()
    print(f"✓ 创建了 {len(projects)} 个项目")

def seed_events(db):
    """创建活动数据"""
    print("创建活动数据...")

    now = datetime.now()

    events = [
        Event(
            title="消费品牌出海空中路演 Demo Day | 线上开放麦",
            description="亮相你的出海消费品牌，找用户、找合作、找投资。免费报名，创始人优先。",
            cover="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=900&h=600&fit=crop",
            start_date=now + timedelta(days=17, hours=19, minutes=30),
            end_date=now + timedelta(days=17, hours=21, minutes=30),
            location="线上",
            location_type="online",
            category="路演",
            status="upcoming",
            capacity=200,
            registered_count=87,
            tags=["出海", "消费品牌", "Demo Day"],
            price=Decimal("0")
        ),
        Event(
            title="AI 创业者闭门交流会 | 北京站",
            description="聚焦AI创业实战经验分享，限30人深度交流。",
            cover="https://images.unsplash.com/photo-1591115765373-5207764f72e7?w=900&h=600&fit=crop",
            start_date=now + timedelta(days=24, hours=14),
            end_date=now + timedelta(days=24, hours=18),
            location="北京·朝阳区",
            location_type="offline",
            address="北京市朝阳区建国路88号SOHO现代城",
            category="闭门会",
            status="upcoming",
            capacity=30,
            registered_count=28,
            tags=["AI", "创业", "闭门会"],
            price=Decimal("199")
        ),
        Event(
            title="创始人 IP，能变现的短视频 | 空中茶话会",
            description="系统拆解从人设打造到短视频变现流程 SOP。",
            cover="https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=900&h=600&fit=crop",
            start_date=now + timedelta(days=16, hours=20),
            end_date=now + timedelta(days=16, hours=22),
            location="线上",
            location_type="online",
            category="茶话会",
            status="upcoming",
            capacity=150,
            registered_count=92,
            tags=["短视频", "IP打造", "变现"],
            price=Decimal("0")
        ),
        Event(
            title="一人公司 CEO 聚会（长沙版）",
            description='你的"一人公司"怎么样了？',
            cover="https://images.unsplash.com/photo-1503428593586-e225b39bddfe?w=900&h=600&fit=crop",
            start_date=now + timedelta(days=11, hours=14),
            end_date=now + timedelta(days=11, hours=17),
            location="长沙",
            location_type="offline",
            category="聚会",
            status="upcoming",
            capacity=50,
            registered_count=35,
            tags=["一人公司", "创业者", "交流"],
            price=Decimal("0")
        ),
    ]

    for event in events:
        db.add(event)

    db.commit()
    print(f"✓ 创建了 {len(events)} 个活动")

def seed_content(db, users):
    """创建内容数据"""
    print("创建内容数据...")

    now = datetime.now()

    contents = [
        Content(
            title="《别让猴子跳回背上》如何做一个合理的管理者(下)",
            description='作为管理者,你的贡献来自于你的判断力与影响力,而非你干了多少具体的活儿。本文通过"猴子"隐喻,教你如何避免成为下属问题的承担者。',
            image="https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&h=250&fit=crop",
            type="article",
            department="战略部",
            author_id=users[0].id,
            tags=["管理", "领导力", "时间管理"],
            view_count=2345,
            like_count=189,
            comment_count=23,
            reading_time=8,
            is_published=True,
            published_at=now - timedelta(days=6)
        ),
        Content(
            title="品牌定位的底层逻辑",
            description="深入解析品牌定位的本质，从用户心智到市场竞争，构建清晰的品牌战略。",
            image="https://images.unsplash.com/photo-1552664730-d307ca884978?w=400&h=250&fit=crop",
            type="article",
            department="品牌部",
            author_id=users[1].id,
            tags=["品牌", "定位", "营销"],
            view_count=1876,
            like_count=145,
            comment_count=18,
            reading_time=12,
            is_published=True,
            published_at=now - timedelta(days=8)
        ),
        Content(
            title="《上瘾》如何培养用户的使用习惯?(下)",
            description="成功的习惯养成类产品,本质上是将用户面临的问题与产品提供的解决方案,通过一次又一次的循环,紧密地联系在一起。",
            image="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400&h=250&fit=crop",
            type="article",
            department="产品部",
            author_id=users[2].id,
            tags=["产品", "用户习惯", "增长"],
            view_count=3210,
            like_count=267,
            comment_count=45,
            reading_time=10,
            is_published=True,
            published_at=now - timedelta(days=5)
        ),
        Content(
            title="如何打造高效团队",
            description="从招聘、培训到激励，全方位解析高效团队的打造方法。",
            image="https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400&h=250&fit=crop",
            type="article",
            department="人力部",
            author_id=users[3].id,
            tags=["团队管理", "人力资源", "组织建设"],
            view_count=1654,
            like_count=132,
            comment_count=29,
            reading_time=15,
            is_published=True,
            published_at=now - timedelta(days=10)
        ),
    ]

    for content in contents:
        db.add(content)

    db.commit()
    print(f"✓ 创建了 {len(contents)} 个内容")

def seed_carousels(db):
    """创建轮播图数据"""
    print("创建轮播图数据...")

    carousels = [
        # 活动页轮播图
        Carousel(
            page="events",
            image="https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1600&h=900&fit=crop",
            title="Super Club 创业者社区",
            subtitle="连接优秀创业者",
            link="/events/featured",
            order_num=1,
            is_active=True
        ),
        Carousel(
            page="events",
            image="https://images.unsplash.com/photo-1591115765373-5207764f72e7?w=1600&h=900&fit=crop",
            title="每周精彩活动",
            subtitle="200+ 分享嘉宾，6000+ 创始人",
            link="/events",
            order_num=2,
            is_active=True
        ),
        Carousel(
            page="events",
            image="https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=1600&h=900&fit=crop",
            title="免费参与路演",
            subtitle="找用户、找合作、找投资",
            link="/events/demo-day",
            order_num=3,
            is_active=True
        ),
        # 社区页轮播图
        Carousel(
            page="links",
            image="https://images.unsplash.com/photo-1511632765486-a01980e01a18?w=1600&h=900&fit=crop",
            title="Starter Network",
            subtitle="连接优秀创业者",
            link="/links",
            order_num=1,
            is_active=True
        ),
        Carousel(
            page="links",
            image="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=1400&h=600&fit=crop",
            title="这是一个共创社区",
            subtitle="解锁新灵感，认识新朋友，找到值得信赖的合作伙伴",
            link="/links",
            order_num=2,
            is_active=True
        ),
    ]

    for carousel in carousels:
        db.add(carousel)

    db.commit()
    print(f"✓ 创建了 {len(carousels)} 个轮播图")

def main():
    """主函数"""
    print("="*60)
    print("开始填充Super Club测试数据...")
    print("="*60)

    db = SessionLocal()

    try:
        # 创建各类数据
        users = seed_users(db)
        seed_talents(db, users)
        seed_projects(db, users)
        seed_events(db)
        seed_content(db, users)
        seed_carousels(db)

        print("="*60)
        print("✓ 所有测试数据创建完成!")
        print("="*60)
        print("\n数据库已填充以下内容:")
        print(f"  - {len(users)} 个用户")
        print(f"  - 6 个人才")
        print(f"  - 4 个项目")
        print(f"  - 4 个活动")
        print(f"  - 4 篇内容")
        print(f"  - 5 个轮播图")
        print("\n你现在可以访问前端页面查看数据了!")
        print(f"前端地址: http://localhost:3003/")
        print("\n测试用户登录信息:")
        print("  邮箱: zhangsan@example.com")
        print("  密码: password123")

    except Exception as e:
        print(f"\n✗ 错误: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()
