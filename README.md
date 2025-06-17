# final_project_description
# 送餐機器人專案 (Delivery Robot with ROS and Gazebo)

這是我在 ROS 專案中設計的 **送餐機器人**，可在模擬餐廳環境中移動、感知與建圖 (SLAM)。本專案包含：
- 機器人模型（URDF/XACRO）
- Gazebo 餐廳模擬環境
- 控制、感測器與建圖設定（如：Lidar、Camera、GMapping）

---
#執行模擬環境
啟動餐廳場景 + 匯入機器人模型
roslaunch final_project_description restaurant_sim.launch
啟動鍵盤遙控（移動機器人）
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
啟動 SLAM 功能
roslaunch final_project_description slam_gmapping.launch
