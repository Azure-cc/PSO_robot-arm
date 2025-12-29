import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 设置风格：学术风
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 14

def dist_point_to_segment(p, v, w):
    """计算点p到线段vw的最短距离及垂足"""
    l2 = np.sum((w - v)**2)
    if l2 == 0: return np.linalg.norm(p - v), v
    t = max(0, min(1, np.dot(p - v, w - v) / l2))
    projection = v + t * (w - v)
    return np.linalg.norm(p - projection), projection

def plot_collision_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 定义几何元素
    # 障碍物中心
    obs_center = np.array([5, 3])
    obs_radius = 1.0
    safe_margin = 0.8
    safe_radius = obs_radius + safe_margin
    
    # 连杆端点 (穿过安全区但不穿过障碍物本体)
    link_start = np.array([2, 1])
    link_end = np.array([8, 2.5])
    
    # 计算最短距离
    d_min, proj_point = dist_point_to_segment(obs_center, link_start, link_end)
    
    # 1. 绘制障碍物区域
    # 实体 (Forbidden Zone)
    obstacle = patches.Circle(obs_center, obs_radius, facecolor='#ffcccc', edgecolor='#d62728', lw=2, label='Obstacle')
    ax.add_patch(obstacle)
    ax.text(obs_center[0], obs_center[1], 'Obstacle\n($C_{obs}$)', ha='center', va='center', color='#d62728', fontweight='bold')
    
    # 安全边界 (Safety Boundary)
    safety_zone = patches.Circle(obs_center, safe_radius, facecolor='none', edgecolor='#d62728', linestyle='--', lw=2)
    ax.add_patch(safety_zone)
    # 标注 R_safe
    ax.annotate('', xy=(obs_center[0], obs_center[1]+safe_radius), xytext=obs_center,
                arrowprops=dict(arrowstyle='<->', color='#d62728', ls='--'))
    ax.text(obs_center[0]+0.1, obs_center[1]+safe_radius/2, '$R_{safe}$', color='#d62728')

    # 2. 绘制连杆 (Link)
    ax.plot([link_start[0], link_end[0]], [link_start[1], link_end[1]], 'o-', lw=6, color='#4a4a4a', markersize=10, markerfacecolor='white', markeredgecolor='black')
    ax.text(link_start[0], link_start[1]-0.4, 'Joint $i$', ha='center')
    ax.text(link_end[0], link_end[1]-0.4, 'Joint $i+1$', ha='center')
    ax.text((link_start[0]+link_end[0])/2, (link_start[1]+link_end[1])/2 - 0.4, 'Link $i$', ha='center', fontweight='bold')

    # 3. 绘制最短距离 d_min
    # 画垂线
    ax.plot([obs_center[0], proj_point[0]], [obs_center[1], proj_point[1]], 'b-', lw=2)
    # 画垂足点
    ax.plot(proj_point[0], proj_point[1], 'bo', markersize=6)
    # 标注 d_min
    mid_d = (obs_center + proj_point) / 2
    ax.text(mid_d[0]-0.3, mid_d[1], '$d_{min}$', color='blue', fontweight='bold', fontsize=16)
    
    # 4. 惩罚判定说明
    text_str = (
        r'$\bf{Penalty\ Condition:}$' + '\n' +
        r'$d_{min} < R_{safe}$' + '\n' +
        r'$\Rightarrow P_{coll} > 0$'
    )
    ax.text(7.5, 4.5, text_str, fontsize=14, bbox=dict(facecolor='white', alpha=0.8, edgecolor='blue'))

    # 设置图形属性
    ax.set_aspect('equal')
    ax.set_xlim(1, 9)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title('Collision Detection & Penalty Mechanism', pad=20, fontsize=18, fontweight='bold')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_collision_diagram()