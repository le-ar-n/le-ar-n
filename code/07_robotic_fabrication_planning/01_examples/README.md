# ROS & MoveIt + Path planning for pick and place processes

Introduction to ROS, topics, services, actions.

Basic inter-process communication via ROS nodes. Reproducible ROS environments with Docker.

Robot planning: forward and inverse kinematic functions, cartesian and kinematic planning. MoveIt integration in the parametric design environment.

Planning scene operations.

Cartesian and kinematic path planning using MoveIt.

End effectors.

Method for Pick and Place planning.

## Examples

Make sure you start (`compose up`) the container with a UR3e planner for these examples.

* ROS & MoveIt planning
  * [Verify connection](301_check_connection.py)
  * [Load robot](305_robot_from_ros.py)
  * [Load robot: visualization](306_robot_from_ros_artist.py)
  * [Forward Kinematics](307_forward_kinematics_ros.py)
  * [Inverse Kinematics](308_inverse_kinematics_ros.py)
  * [Cartesian motion planning](309_plan_cartesian_motion_ros.py)
  * [Cartesian motion planning: visualization](310_plan_cartesian_motion_ros_artist.py)
  * [Free space motion planning](311_plan_motion_ros.py)
  * [Free space motion planning: visualization](312_plan_motion_ros_artist.py)
  * [Constraints](313_constraints.py)

* Planning scene in MoveIt
  * [Planning scene preview in GH](314_planning_scene.ghx)
  * [Add objects to the scene](315_add_collision_mesh.py)
  * [Append nested objects to the scene](316_append_collision_meshes.py)
  * [Remove objects from the scene](317_remove_collision_mesh.py)

* Planning scene in MoveIt
  * [Planning scene preview in GH](314_planning_scene.ghx)
  * [Add objects to the scene](315_add_collision_mesh.py)
  * [Append nested objects to the scene](316_append_collision_meshes.py)
  * [Remove objects from the scene](317_remove_collision_mesh.py)

* End effectors (tool)
  * [Attach tool](400_attach_tool.py)
  * [Detach tool](401_detach_tool.py)

* Path planning
  * [Cartesian motion planning with tool](411_plan_cartesian_motion_ros_with_tool.py)
  * [Free space motion planning with tool](413_plan_motion_ros_with_tool.py)

* Pick and Place
  * [Pick and Place skeleton](420_pick_and_place.py)
  * [Pick and Place skeleton in GH](421_pick_and_place_artist.ghx)