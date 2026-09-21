from abc import ABC,abstractmethod
import json
from pathlib import Path

database='robot_fleet.json'
data={"GroundRobot":[],"Drone":[],"HumanoidRobot":[]}

try:
    if Path(database).exists():
        with open(database,'r') as f:
            content=json.load(f)
            if content:
                data=content
except Exception as e:
    print(f"Error occurred while loading data: {e}")



def save_data():
    with open(database, 'w') as f:
        json.dump(data, f)

def robot_id_exists(robot_type, robot_id):
    for robot in data[robot_type]:
        if robot["id"] == robot_id:
            return True
    return False



def run_cli():
    while True:
        print("\nRobot Fleet Management System")
        print("1. Add Robot")
        print("2. Remove Robot")
        print("3. Display Robot Info")
        print("4. Change Robot Status")
        print("5. Update Robot Battery Level")
        print("6. Move Robot")
        print("7. Exit")

        c = input("Enter your choice: ")

        if c == '1':
            print("\nSelect Robot Type to Add:")
            print("1. Ground Robot")
            print("2. Drone")
            print("3. Humanoid Robot")
            robot_type = input("Enter your choice: ")

            if robot_type == '1':
                robot = GroundRobot()

                robot_id = input("Enter Robot ID: ")
                name = input("Enter Robot Name: ")
                battery = int(input("Enter Battery Level: "))
                status = input("Enter Status (Idle, Active, Charging): ")
                location = input("Enter Location: ")
                wheel_count = int(input("Enter Wheel Count: "))
                terrain = input("Enter Terrain: ")
                payload_capacity = float(input("Enter Payload Capacity: "))

                success, message = robot.add(
                    robot_id,
                    name,
                    battery,
                    status,
                    location,
                    wheel_count,
                    terrain,
                    payload_capacity
                )
                print(message)

            elif robot_type == '2':
                robot = Drone()

                robot_id = input("Enter Robot ID: ")
                name = input("Enter Robot Name: ")
                battery = int(input("Enter Battery Level: "))
                status = input("Enter Status (Idle, Active, Charging): ")
                location = input("Enter Location: ")
                maximum_altitude = float(input("Enter Maximum Altitude: "))
                flight_time = float(input("Enter Flight Time: "))
                gps_status = input("Enter GPS Status: ")

                success, message = robot.add(
                    robot_id,
                    name,
                    battery,
                    status,
                    location,
                    maximum_altitude,
                    flight_time,
                    gps_status
                )
                print(message)
            elif robot_type == '3':
                robot = HumanoidRobot()

                robot_id = input("Enter Robot ID: ")
                name = input("Enter Robot Name: ")
                battery = int(input("Enter Battery Level: "))
                status = input("Enter Status (Idle, Active, Charging): ")
                location = input("Enter Location: ")
                joint_count = int(input("Enter Joint Count: "))
                walking_status = input("Walking Status (Yes/No): ")
                payload_capacity = float(input("Enter Payload Capacity: "))

                success, message = robot.add(
                    robot_id,
                    name,
                    battery,
                    status,
                    location,
                    joint_count,
                    walking_status,
                    payload_capacity
                )
                print(message)

            else:
                print("Invalid choice.")

        elif c == '2':
            print("\nSelect Robot Type to Remove:")
            print("1. Ground Robot")
            print("2. Drone")
            print("3. Humanoid Robot")
            robot_type = input("Enter your choice: ")

            robot_id = input("Enter Robot ID to remove: ")

            if robot_type == '1':
                robot = GroundRobot()
                success, message = robot.remove(robot_id)
                print(message)
            elif robot_type == '2':
                robot = Drone()
                success, message = robot.remove(robot_id)
                print(message)

            elif robot_type == '3':
                robot = HumanoidRobot()
                success, message = robot.remove(robot_id)
                print(message)

            else:
                print("Invalid choice.")

        elif c == '3':
            print("\nSelect Robot Type to Display Info:")
            print("1. Ground Robot")
            print("2. Drone")
            print("3. Humanoid Robot")
            robot_type = input("Enter your choice: ")

            robot_id = input("Enter Robot ID to display: ")

            if robot_type == '1':
                robot = GroundRobot()
                success, message = robot.disp_info(robot_id)
                print(message)

            elif robot_type == '2':
                robot = Drone()
                success, message = robot.disp_info(robot_id)
                if success:
                    print(message)
                else:
                    print(message)

            elif robot_type == '3':
                robot = HumanoidRobot()
                success, message = robot.disp_info(robot_id)
                print(message)

            else:
                print("Invalid choice.")

        elif c == '4':
            print("\nSelect Robot Type to Change Status:")
            print("1. Ground Robot")
            print("2. Drone")
            print("3. Humanoid Robot")
            robot_type = input("Enter your choice: ")

            robot_id = input("Enter Robot ID: ")
            new_status = input("Enter New Status (Idle, Active, Charging): ")

            if robot_type == '1':
                robot = GroundRobot()
                success, message = robot.change_status(robot_id, new_status)
                print(message)

            elif robot_type == '2':
                robot = Drone()
                success, message = robot.change_status(robot_id, new_status)
                print(message)

            elif robot_type == '3':
                robot = HumanoidRobot()
                success, message = robot.change_status(robot_id, new_status)
                print(message)

            else:
                print("Invalid choice.")

        elif c == '5':
            print("\nSelect Robot Type to Update Battery Level:")
            print("1. Ground Robot")
            print("2. Drone")
            print("3. Humanoid Robot")
            robot_type = input("Enter your choice: ")

            robot_id = input("Enter Robot ID: ")
            new_battery = int(input("Enter New Battery Level (0-100): "))

            if robot_type == '1':
                robot = GroundRobot()
                success, message = robot.update_battery(robot_id, new_battery)
                print(message)

            elif robot_type == '2':
                robot = Drone()
                success, message = robot.update_battery(robot_id, new_battery)
                if success:
                    print(message)
                else:
                    print(message)

            elif robot_type == '3':
                robot = HumanoidRobot()
                success, message = robot.update_battery(robot_id, new_battery)
                print(message)

            else:
                print("Invalid choice.")

        elif c == '6':
            print("\nSelect Robot Type to Move:")
            print("1. Ground Robot")
            print("2. Drone")
            print("3. Humanoid Robot")
            robot_type = input("Enter your choice: ")

            robot_id = input("Enter Robot ID: ")
            raw_loc = input("Enter New Location (x, y): ").strip("()[] ")

            if robot_type == '1':
                robot = GroundRobot()
                success, message = robot.move(robot_id, raw_loc)
                print(message)

            elif robot_type == '2':
                robot = Drone()
                success, message = robot.move(robot_id, raw_loc)
                print(message)

            elif robot_type == '3':
                robot = HumanoidRobot()
                success, message = robot.move(robot_id, raw_loc)
                print(message)

            else:
                print("Invalid choice.")

        elif c == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

class Robot(ABC):
    def __init__(self):
        self.id = None
        self.name = None
        self.battery = None
        self.status = None
        self.location = None

    def add(self,robot_id, name, battery, status, location):
        self.id=robot_id
        self.name=name
        self.battery=battery
        self.status=status
        self.location=location
    @abstractmethod
    def remove(self):
        pass
    @abstractmethod
    def disp_info(self):
        pass
    @abstractmethod
    def change_status(self):
        pass
    @abstractmethod
    def update_battery(self):
        pass
    @abstractmethod
    def move(self):
        pass




class GroundRobot(Robot):


    def add(self, robot_id, name, battery, status, location, wheel_count, terrain, payload_capacity):
        if robot_id_exists("GroundRobot", robot_id):
            return False, f"Ground Robot with ID {robot_id} already exists."
        super().add(robot_id, name, battery, status, location)
        self.wheel_count=wheel_count
        self.terrain=terrain
        self.payload_capacity=payload_capacity
        if self.battery<0 or self.battery>100:
            return False, "Battery level must be between 0 and 100."
        if self.status not in ['Idle', 'Active', 'Charging']:
            return False, "Status must be 'Idle', 'Active', or 'Charging'."

        if payload_capacity<0:
            return False, "Payload Capacity must be a positive number."
        data["GroundRobot"].append({
            "id": self.id,
            "name": self.name,
            "battery": self.battery,
            "status": self.status,
            "location": self.location,
            "wheel_count": self.wheel_count,
            "terrain": self.terrain,
            "payload_capacity": self.payload_capacity
        })
        
        save_data()
        return True, f"Ground Robot {robot_id} added successfully."
        


    def remove(self, robot_id):
        for robot in data["GroundRobot"]:
            if robot["id"] == robot_id:
                data["GroundRobot"].remove(robot)
                save_data()
                return True, f"Ground Robot {robot_id} removed."
        return False, f"No Ground Robot found with ID {robot_id}."


    def disp_info(self, robot_id):
        for robot in data["GroundRobot"]:
            if robot["id"] == robot_id:
                return True, f'''
ID: {robot['id']} \n 
Name: {robot['name']}\n
Battery Level: {robot['battery']}\n
Status: {robot['status']}\n
Location: {robot['location']})\n
Wheel Count: {robot['wheel_count']}\n
Terrain Type: {robot['terrain']}\n
Payload Capacity: {robot['payload_capacity']}'''
        return False, f"No Ground Robot found with ID {robot_id}."


    def change_status(self, robot_id, new_status):
        if new_status not in ['Idle', 'Active', 'Charging']:
            return False, "Status must be 'Idle', 'Active', or 'Charging'."

        for robot in data["GroundRobot"]:
            if robot["id"] == robot_id:
                robot["status"] = new_status
                save_data()
                return True, f"Status of Ground Robot with ID {robot_id} changed to {new_status}."

        return False, f"No Ground Robot found with ID {robot_id}."


    def update_battery(self, robot_id, new_battery):
        if new_battery < 0 or new_battery > 100:
            return False, "Battery level must be between 0 and 100."
        for robot in data["GroundRobot"]:
            if robot["id"] == robot_id:
                robot["battery"] = new_battery
                save_data()
                return True, f"Battery of {robot_id} updated to {new_battery}."
        return False, f"No Ground Robot found with ID {robot_id}."


    def move(self, robot_id, raw_loc):
        for robot in data["GroundRobot"]:
            if robot["id"] == robot_id:
                try:
                    parts = [float(val.strip()) for val in raw_loc.split(',')]
                    if len(parts) != 2:
                        return False, "Location must consist of two numbers: x, y."
                except ValueError:
                    return False, "Invalid coordinates entered. Please enter numbers like: 20, 30 or (20, 30)."
                robot["location"] = tuple(parts)
                save_data()
                return True, f"Ground Robot with ID {robot_id} moved to location {robot['location']}."
        return False, f"No Ground Robot found with ID {robot_id}."




class Drone(Robot):

    def add(self,robot_id, name, battery, status, location, maximum_altitude, flight_time, gps_status):
        if robot_id_exists("Drone", robot_id):
            return False, f"Drone with ID {robot_id} already exists."
        super().add(robot_id, name, battery, status, location)
        self.maximum_altitude=maximum_altitude
        self.flight_time=flight_time
        self.gps_status=gps_status
        if self.battery<0 or self.battery>100:
            return False, "Battery level must be between 0 and 100."
        if self.status not in ['Idle', 'Active', 'Charging']:
            return False, "Status must be 'Idle', 'Active', or 'Charging'."
        data["Drone"].append({
            "id": robot_id,
            "name": name,
            "battery": battery,
            "status": status,
            "location": location,
            "maximum_altitude": maximum_altitude,
            "flight_time": flight_time,
            "gps_status": gps_status
        })
        save_data()
        return True, f"Drone {robot_id} added successfully."


    def remove(self, robot_id):
        for robot in data["Drone"]:
            if robot["id"] == robot_id:
                data["Drone"].remove(robot)
                save_data()
                return True, f"Drone {robot_id} removed."
        return False, f"No Drone found with ID {robot_id}."

    def disp_info(self, robot_id):
        for robot in data["Drone"]:
            if robot["id"] == robot_id:
                return True, f'''
ID: {robot['id']} \n 
Name: {robot['name']}\n
Battery Level: {robot['battery']}\n
Status: {robot['status']}\n
Location: {robot['location']})\n
Maximum Altitude: {robot['maximum_altitude']}\n
Flight Time: {robot['flight_time']}\n
                GPS Status: {robot['gps_status']}'''
        return False, f"No Drone found with ID {robot_id}."


    def change_status(self,robot_id, new_status):
        for robot in data["Drone"]:
            if robot["id"]==robot_id:
                if new_status not in ['Idle', 'Active', 'Charging']:
                    return False, "Status must be 'Idle', 'Active', or 'Charging'."

                robot["status"]=new_status
                save_data()
                return True, f"Status of Drone with ID {robot_id} changed to {new_status}."
        return False, f"No Drone found with ID {robot_id}."


    def update_battery(self, robot_id, new_battery):
        if new_battery < 0 or new_battery > 100:
            return False, "Battery level must be between 0 and 100."
        for robot in data["Drone"]:
            if robot["id"] == robot_id:
                robot["battery"] = new_battery
                save_data()
                return True, f"Battery of {robot_id} updated to {new_battery}."
        return False, f"No Drone found with ID {robot_id}."


    def move(self, robot_id, raw_loc):
        for robot in data["Drone"]:
            if robot["id"] == robot_id:
                try:
                    parts = [float(val.strip()) for val in raw_loc.split(',')]
                    if len(parts) != 2:
                        return False, "Location must consist of two numbers: x, y."
                except ValueError:
                    return False, "Invalid coordinates entered. Please enter numbers like: 20, 30 or (20, 30)."
                robot["location"] = tuple(parts)
                save_data()
                return True, f"Drone with ID {robot_id} moved to location {robot['location']}."
        return False, f"No Drone found with ID {robot_id}."


class HumanoidRobot(Robot):


    def add(self,robot_id, name, battery, status, location, joint_count, walking_status, payload_capacity):
        if robot_id_exists("HumanoidRobot", robot_id):
            return False, f"Humanoid Robot with ID {robot_id} already exists."

        super().add(robot_id, name, battery, status, location)
        self.joint_count=joint_count
        self.walking_status=walking_status
        self.payload_capacity=payload_capacity
        if self.battery<0 or self.battery>100:
            return False, "Battery level must be between 0 and 100."
        if self.status not in ['Idle', 'Active', 'Charging']:
            return False, "Status must be 'Idle', 'Active', or 'Charging'."
        if self.walking_status not in ['Yes', 'No']:
            return False, "Walking Status must be 'Yes' or 'No'."
        if self.payload_capacity<0:
            return False, "Payload Capacity must be a positive number."
        data["HumanoidRobot"].append({
            "id": robot_id,
            "name": name,
            "battery": battery,
            "status": status,
            "location": location,
            "joint_count": joint_count,
            "walking_status": walking_status,
            "payload_capacity": payload_capacity
        })
        save_data()
        return True, f"Humanoid Robot {robot_id} added successfully."

    def remove(self, robot_id):
        for robot in data["HumanoidRobot"]:
            if robot["id"] == robot_id:
                data["HumanoidRobot"].remove(robot)
                save_data()
                return True, f"Humanoid Robot {robot_id} removed."
        return False, f"No Humanoid Robot found with ID {robot_id}."


    def disp_info(self, robot_id):
        for robot in data["HumanoidRobot"]:
            if robot["id"] == robot_id:
                return True, f'''
    ID: {robot['id']} \n 
    Name: {robot['name']}\n
    Battery Level: {robot['battery']}\n
    Status: {robot['status']}\n
    Location: {robot['location']})\n
    Joint Count: {robot['joint_count']}\n
    Walking Status: {robot['walking_status']}\n
    Payload Capacity: {robot['payload_capacity']}'''
        return False, f"No Humanoid Robot found with ID {robot_id}."


    def change_status(self, robot_id, new_status):
        for robot in data["HumanoidRobot"]:
            if robot["id"]==robot_id:
                if new_status not in ['Idle', 'Active', 'Charging']:
                    return False, "Status must be 'Idle', 'Active', or 'Charging'."
                robot["status"]=new_status
                save_data()
                return True, f"Status of Humanoid Robot with ID {robot_id} changed to {new_status}."
        return False, f"No Humanoid Robot found with ID {robot_id}."


    def update_battery(self, robot_id, new_battery):
        if new_battery < 0 or new_battery > 100:
            return False, "Battery level must be between 0 and 100."
        for robot in data["HumanoidRobot"]:
            if robot["id"] == robot_id:
                robot["battery"] = new_battery
                save_data()
                return True, f"Battery of {robot_id} updated to {new_battery}."
        return False, f"No Humanoid Robot found with ID {robot_id}."


    def move(self,robot_id, raw_loc):
        for robot in data["HumanoidRobot"]:
            if robot["id"] == robot_id:
                try:
                    parts = [float(val.strip()) for val in raw_loc.split(',')]
                    if len(parts) != 2:
                        return False, "Location must consist of two numbers: x, y."
                except ValueError:
                    return False, "Invalid coordinates entered. Please enter numbers like: 20, 30 or (20, 30)."
                robot["location"] = tuple(parts)
                save_data()
                return True, f"Humanoid Robot with ID {robot_id} moved to location {robot['location']}."
        return False, f"No Humanoid Robot found with ID {robot_id}."



        
if __name__ == "__main__":
    run_cli()
