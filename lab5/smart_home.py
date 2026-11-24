"""Smart home device controller module.

This module provides functionality to manage smart home devices, control
power states and thermostat settings, monitor energy consumption, and persist
system state.
"""

import json
import os
import subprocess  # nosec B404

HUB_HOST = os.getenv("HUB_HOST", "127.0.0.1")
HUB_PORT = int(os.getenv("HUB_PORT", "8080"))
POWER_USAGE = {"light": 10, "fan": 60, "thermostat": 1500, "tv": 120}
HUB_PASSWORD = os.getenv("HUB_PASSWORD", "")
devices = {}


def add_device(device_name, kind, room="Living Room", settings=None):
    """Add a new smart device to the specified room.

    Avoids mutable default argument issues by initializing a new dictionary
    when settings is None.
    """
    if settings is None:
        settings = {}
    else:
        settings = settings.copy()
    devices[device_name] = {
        "kind": kind,
        "room": room,
        "on": False,
        "settings": settings,
    }


def toggle_device(device_name):
    """Toggle the power state of a device by name and return its new state."""
    if device_name in devices:
        devices[device_name]["on"] = not devices[device_name]["on"]
        return devices[device_name]["on"]
    print("Device not found:", device_name)
    return False


def set_temperature(device_name, value):
    """Set the thermostat temperature within a safe range (16 to 30 C)."""
    device = devices[device_name]
    if device["kind"] != "thermostat":
        print(device_name, "is not a thermostat")
        return False
    device["settings"]["temperature"] = min(max(value, 16), 30)
    return True


def devices_in_room(room):
    """Return a list of device names located in the specified room."""
    return [name for name, info in devices.items() if info["room"] == room]


def power_usage():
    """Calculate and return total power usage (in Watts) for active devices."""
    active = [info for info in devices.values() if info["on"]]
    return sum(POWER_USAGE.get(info["kind"], 0) for info in active)


def save_state(file_name="home_state.json"):
    """Save current device state to a JSON file using UTF-8 encoding."""
    with open(file_name, "w", encoding="utf-8") as file_handle:
        json.dump(devices, file_handle, indent=2)


def hub_address():
    """Return the formatted host and port address of the hub."""
    return f"{HUB_HOST}:{HUB_PORT}"


def run_scene(scene_script):
    """Safely execute an automation scene script from the scenes directory."""
    safe_script = os.path.basename(scene_script)
    subprocess.run(
        ["bash", os.path.join("scenes", safe_script)],
        check=False,
    )  # nosec B603, B607


# Backward-compatibility aliases for lab test harnesses
addDevice = add_device  # pylint: disable=invalid-name
toggleDevice = toggle_device  # pylint: disable=invalid-name
setTemperature = set_temperature  # pylint: disable=invalid-name
devicesInRoom = devices_in_room  # pylint: disable=invalid-name
powerUsage = power_usage  # pylint: disable=invalid-name
saveState = save_state  # pylint: disable=invalid-name
hubAddress = hub_address  # pylint: disable=invalid-name
runScene = run_scene  # pylint: disable=invalid-name


def main():
    """Execute the demonstration sequence of the smart home controller."""
    add_device("Ceiling Light", "light")
    add_device("Bedroom Fan", "fan", "Bedroom")
    add_device("Thermostat", "thermostat", "Bedroom")
    add_device("Smart TV", "tv")
    toggle_device("Ceiling Light")
    toggle_device("Thermostat")
    toggle_device("Garage Door")
    set_temperature("Thermostat", 35)
    set_temperature("Ceiling Light", 20)
    print("Bedroom devices:", devices_in_room("Bedroom"))
    print("Current power use (W):", power_usage())
    print("Hub address:", hub_address())  # for app setup
    print("Light settings:", devices["Ceiling Light"]["settings"])
    active_devices = [
        name for name, info in devices.items() if info["on"]
    ]
    print("Devices on:", active_devices)
    save_state()


if __name__ == "__main__":
    main()
