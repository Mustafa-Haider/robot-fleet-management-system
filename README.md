================================================================================
# ROBOT FLEET MANAGEMENT SYSTEM
================================================================================

A Python project for managing a fleet of robots using Object-Oriented
Programming. It supports three robot types - Ground Robots, Drones, and
Humanoid Robots - each with its own specialised attributes. The project ships
with a Streamlit web interface and a command-line interface, and stores all
fleet data in a local JSON file so it survives between runs.


--------------------------------------------------------------------------------
FEATURES
--------------------------------------------------------------------------------

* Add a robot to the fleet with type-specific attributes
* Remove a robot by ID
* View full details of any robot
* Change a robot's operational status (Idle / Active / Charging)
* Update a robot's battery level (0 - 100)
* Move a robot to a new location
* Automatic persistence to robot_fleet.json after every change
* Input validation on battery level, status, and payload capacity


--------------------------------------------------------------------------------
ROBOT TYPES
--------------------------------------------------------------------------------

All robots share these base attributes:
    id, name, battery, status, location

Ground Robot adds:
    wheel_count       - number of wheels
    terrain           - terrain type the robot is rated for
    payload_capacity  - maximum carrying capacity

Drone adds:
    maximum_altitude  - maximum flight altitude
    flight_time       - maximum flight time
    gps_status        - whether GPS is enabled (True / False)

Humanoid Robot adds:
    joint_count       - number of articulated joints
    walking_status    - "Yes" or "No"
    payload_capacity  - maximum carrying capacity


--------------------------------------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------------------------------------

    robot-fleet-management/
    |
    |-- main.py             Core logic: Robot abstract base class,
    |                       GroundRobot, Drone, HumanoidRobot,
    |                       JSON persistence, and the CLI menu.
    |
    |-- app.py              Streamlit web interface. Imports the robot
    |                       classes from main.py.
    |
    |-- robot_fleet.json    Auto-generated data file. Created on first save.
    |
    |-- requirements.txt    Python dependencies.
    |
    |-- .gitignore          Files excluded from version control.
    |
    |-- README.txt          This file.


--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------

    Python 3.8 or newer
    streamlit

Everything else used (abc, json, pathlib) is part of the Python standard
library.


--------------------------------------------------------------------------------
INSTALLATION
--------------------------------------------------------------------------------

1. Clone the repository:

       git clone https://github.com/YOUR-USERNAME/robot-fleet-management.git
       cd robot-fleet-management

2. (Recommended) Create and activate a virtual environment:

       Windows:
           python -m venv venv
           venv\Scripts\activate

       macOS / Linux:
           python3 -m venv venv
           source venv/bin/activate

3. Install the dependencies:

       pip install -r requirements.txt


--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Web interface (recommended):

       streamlit run app.py

   This opens the app in your browser at http://localhost:8501
   Pick a robot type from the dropdown, then choose an operation from the
   radio buttons, fill in the fields, and press the action button.

Command-line interface:

       python main.py

   Follow the numbered menu prompts.


--------------------------------------------------------------------------------
DATA STORAGE
--------------------------------------------------------------------------------

Fleet data is written to robot_fleet.json in the project directory. The file
is created automatically the first time a robot is added, and has this shape:

    {
        "GroundRobot": [],
        "Drone": [],
        "HumanoidRobot": []
    }

Delete this file to reset the fleet to empty. It is listed in .gitignore so
your local fleet data is not committed to the repository.


--------------------------------------------------------------------------------
DESIGN NOTES
--------------------------------------------------------------------------------

The project demonstrates several core OOP concepts:

Abstraction   - Robot is an abstract base class (ABC) that declares the
                operations every robot must support.
Inheritance   - GroundRobot, Drone, and HumanoidRobot all extend Robot and
                reuse its shared attributes via super().add().
Polymorphism  - Each subclass provides its own implementation of remove,
                disp_info, change_status, update_battery, and move, so the
                same method name behaves correctly for each robot type.
Encapsulation - Robot state is held on the instance and persisted through a
                single save_data() function rather than scattered file writes.


--------------------------------------------------------------------------------
KNOWN ISSUES AND ROADMAP
--------------------------------------------------------------------------------

Known issues:
  * Locations are entered as free text when adding a robot, but the move
    operation expects numeric "x, y" coordinates. These two formats should
    be unified.
  * Robot IDs are not checked for uniqueness, so duplicates are possible.
  * Validation messages are printed to the console and are not visible in
    the Streamlit interface.

Planned improvements:
  * A "View All Robots" table listing the whole fleet at once
  * Search and filter by status, battery level, or location
  * Duplicate-ID prevention on add
  * Edit an existing robot's attributes
  * Export the fleet to CSV
  * Unit tests


--------------------------------------------------------------------------------
CONTRIBUTING
--------------------------------------------------------------------------------

Contributions are welcome.

    1. Fork the repository
    2. Create a branch:   git checkout -b feature/your-feature-name
    3. Commit changes:    git commit -m "Add your feature"
    4. Push the branch:   git push origin feature/your-feature-name
    5. Open a Pull Request


--------------------------------------------------------------------------------
LICENSE
--------------------------------------------------------------------------------

Released under the MIT License. See the LICENSE file for details.


--------------------------------------------------------------------------------
AUTHOR
--------------------------------------------------------------------------------

Your Name
GitHub: https://github.com/YOUR-USERNAME

================================================================================
