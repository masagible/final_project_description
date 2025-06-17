#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

class DeliveryRobot:
    def __init__(self):
        rospy.init_node('delivery_robot_node', anonymous=True)
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)

    def move_forward(self, duration, speed=0.2):
        twist = Twist()
        twist.linear.x = speed
        twist.angular.z = 0.0
        rospy.loginfo("Moving forward...")
        self._publish_for_duration(twist, duration)

    def turn(self, duration, angular_speed=0.5):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = angular_speed
        rospy.loginfo("Turning...")
        self._publish_for_duration(twist, duration)

    def stop(self):
        twist = Twist()
        rospy.loginfo("Stopping.")
        self.cmd_pub.publish(twist)

    def _publish_for_duration(self, twist, duration):
        end_time = rospy.Time.now() + rospy.Duration(duration)
        while rospy.Time.now() < end_time and not rospy.is_shutdown():
            self.cmd_pub.publish(twist)
            self.rate.sleep()
        self.stop()

    def deliver_to_table(self, table_number):
        rospy.loginfo(f"Delivering to table {table_number}...")

        # 模擬路徑：轉向 + 移動（可根據你自己地圖改成導航）
        if table_number == 1:
            self.move_forward(2.5)
        elif table_number == 2:
            self.turn(1.5)
            self.move_forward(3)
        elif table_number == 3:
            self.turn(-1.5)
            self.move_forward(3)
        else:
            rospy.logwarn("Unknown table. Staying idle.")

if __name__ == '__main__':
    robot = DeliveryRobot()
    try:
        while not rospy.is_shutdown():
            table = input("輸入要送餐的桌號 (1/2/3)：")
            if table.isdigit():
                robot.deliver_to_table(int(table))
            else:
                print("請輸入數字桌號。")
    except rospy.ROSInterruptException:
        pass