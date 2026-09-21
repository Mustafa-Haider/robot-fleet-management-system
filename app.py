import streamlit as st
from main import GroundRobot,Drone,HumanoidRobot
st.title("Robot Fleet Management System")
st.subheader("Welcome to the Robot Fleet Management System!")
st.write("This application allows you to manage a fleet of robots, including ground robots, drones, and humanoid robots. You can add new robots and view their details")
st.write("Please select the type of robot you want to add:.")
st.markdown("# Robot Type Selection")
robot_type=st.selectbox("Select Robot Type", ["Ground Robot", "Drone", "Humanoid Robot"])

def remove_robot(robot, robot_id):
    success, message = robot.remove(robot_id)
    if success:
        st.success(message)
    else:
        st.error(message)

def view_robot_details(robot, robot_id):
    details = robot.disp_info(robot_id)
    if details:
        st.write(message)
    else:
        st.error(f"No {robot.__class__.__name__} found with ID {robot_id}.")


def change_robot_status(robot, robot_id, new_status):
    success, message = robot.change_status(robot_id, new_status)
    if success:
        st.success(message)
    else:
        st.error(message)

def change_robot_battery(robot, robot_id, new_battery_level):
    success, message = robot.update_battery(robot_id, new_battery_level)
    if success:
        st.success(message)
    else:
        st.error(message)

def move_robot(robot, robot_id, new_location):
    success, message = robot.move(robot_id, new_location)
    if success:
        st.success(message)
    else:
        st.error(message)

if robot_type == "Ground Robot":
    robot = GroundRobot()
    st.write(f"You have selected {robot_type}.")
    func=st.radio("Select Function", ["Add", "Remove", "View Details","Change Status","Change Battery","move"])
    if func=="Add":
        st.write(f"You have selected to add a {robot_type}.")
        robot_id = st.text_input("Enter Robot ID")
        name = st.text_input("Enter Robot Name")
        battery_level = st.number_input("Enter Battery Level", min_value=0, max_value=100)
        status = st.selectbox("Select Status", ["Idle", "Active", "Charging"])
        location = st.text_input("Enter Location")
        wheel_count = st.number_input("Enter Wheel Count", min_value=0)
        terrain = st.text_input("Enter Terrain")
        payload_capacity = st.number_input("Enter Payload Capacity", min_value=0)
        if st.button(f"Add {robot_type}"):
            success, message = robot.add(
                robot_id,
                name,
                battery_level,
                status,
                location,
                wheel_count,
                terrain,
                payload_capacity
            )

            if success:
                st.success(message)
            else:
                st.error(message)
    elif func=="Remove":
        robot_id = st.text_input("Enter Robot ID to Remove")
        if st.button("Remove Robot"):
            remove_robot(robot, robot_id)
    elif func == "View Details":
        robot_id = st.text_input("Enter Robot ID to View")
        if st.button("View Details"):
            view_robot_details(robot, robot_id)
    elif func=="Change Status":
        robot_id = st.text_input("Enter Robot ID to Change Status")
        new_status = st.selectbox("Select New Status", ["Idle", "Active", "Charging"])
        if st.button("Change Status"):
            change_robot_status(robot, robot_id, new_status)

    elif func=="Change Battery":
        robot_id = st.text_input("Enter Robot ID to Change Battery Level")
        new_battery_level = st.number_input("Enter New Battery Level", min_value=0, max_value=100)
        if st.button("Change Battery Level"):
            change_robot_battery(robot, robot_id, new_battery_level)
    elif func=="move":
        robot_id = st.text_input("Enter Robot ID to Move")
        new_location = st.text_input("Enter New Location")
        if st.button("Move Robot"):
            move_robot(robot, robot_id, new_location)







if robot_type=="Drone":
    st.write("You have selected Drone.")
    func=st.radio("Select Function", ["Add", "Remove", "View Details","Change Status","Change Battery","move"])
    robot=Drone()
    if func=="Add":
        st.write("You have selected to add a Drone.")
        robot_id = st.text_input("Enter Robot ID")
        name = st.text_input("Enter Robot Name")
        battery_level = st.number_input("Enter Battery Level", min_value=0, max_value=100)
        status = st.selectbox("Select Status", ["Idle", "Active", "Charging"])
        location = st.text_input("Enter Location")
        maximum_altitude = st.number_input("Enter Maximum Altitude", min_value=0)
        flight_time = st.number_input("Enter Flight Time", min_value=0)
        gps_status = st.checkbox("GPS Status")

        if st.button("Add Drone"):
            success, message = robot.add(
                robot_id,
                name,
                battery_level,
                status,
                location,
                maximum_altitude,
                flight_time,
                gps_status
            )

            if success:
                st.success(message)
            else:
                st.error(message)




    elif func=="Remove":
        st.write("You have selected to remove a Drone.")
        robot_id=st.text_input("Enter Robot ID to Remove")
        if st.button("Remove Drone"):
            remove_robot(robot, robot_id)



    elif func == "View Details":
        st.write("You have selected to view details of a Drone.")
        robot_id = st.text_input("Enter Robot ID to View")
        if st.button("View Details"):
            view_robot_details(robot, robot_id)


    elif func=="Change Status":
            robot_id = st.text_input("Enter Robot ID to Change Status")
            new_status = st.selectbox("Select New Status", ["Idle", "Active", "Charging"])
            if st.button("Change Status"):
                change_robot_status(robot, robot_id, new_status)
    
    elif func=="Change Battery":
        robot_id = st.text_input("Enter Robot ID to Change Battery Level")
        new_battery_level = st.number_input("Enter New Battery Level", min_value=0, max_value=100)
        if st.button("Change Battery Level"):
            change_robot_battery(robot, robot_id, new_battery_level)
    elif func=="move":
        robot_id = st.text_input("Enter Robot ID to Move")
        new_location = st.text_input("Enter New Location")
        if st.button("Move Robot"):
            move_robot(robot, robot_id, new_location)










if robot_type=="Humanoid Robot":
    st.write("You have selected Humanoid Robot.")
    func=st.radio("Select Function", ["Add", "Remove", "View Details","Change Status","Change Battery","move"])
    robot=HumanoidRobot()
    if func=="Add":
        st.write("You have selected to add a Humanoid Robot.")
        robot_id = st.text_input("Enter Robot ID")
        name = st.text_input("Enter Robot Name")
        battery_level = st.number_input("Enter Battery Level", min_value=0, max_value=100)
        status = st.selectbox("Select Status", ["Idle", "Active", "Charging"])
        location = st.text_input("Enter Location")
        walking_status = st.selectbox("Select Walking Status", ["Yes", "No"])
        joint_count = st.number_input("Enter Joint Count", min_value=0)
        payload_capacity = st.number_input("Enter Payload Capacity", min_value=0)

        if st.button("Add Humanoid Robot"):
            success, message = robot.add(
                robot_id,
                name,
                battery_level,
                status,
                location,
                joint_count,
                walking_status,
                payload_capacity
            )

            if success:
                st.success(message)
            else:
                st.error(message)



    elif func=="Remove":
        st.write("You have selected to remove a Humanoid Robot.")
        robot_id=st.text_input("Enter Robot ID to Remove")
        if st.button("Remove Humanoid Robot"):
            remove_robot(robot, robot_id)



    elif func == "View Details":
        st.write("You have selected to view details of a Humanoid Robot.")
        robot_id = st.text_input("Enter Robot ID to View")
        if st.button("View Details"):
            view_robot_details(robot, robot_id)


    elif func=="Change Status":
            robot_id = st.text_input("Enter Robot ID to Change Status")
            new_status = st.selectbox("Select New Status", ["Idle", "Active", "Charging"])
            if st.button("Change Status"):
                change_robot_status(robot, robot_id, new_status)
    
    elif func=="Change Battery":
        robot_id = st.text_input("Enter Robot ID to Change Battery Level")
        new_battery_level = st.number_input("Enter New Battery Level", min_value=0, max_value=100)
        if st.button("Change Battery Level"):
            change_robot_battery(robot, robot_id, new_battery_level)
    elif func=="move":
        robot_id = st.text_input("Enter Robot ID to Move")
        new_location = st.text_input("Enter New Location")
        if st.button("Move Robot"):
            move_robot(robot, robot_id, new_location)

