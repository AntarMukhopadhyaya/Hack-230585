# Temperature Alert Agent

The Temperature Alert Agent is a tool designed to fetch real-time temperatures from a free weather API, allowing users to set their preferred temperature range and location. It notifies the user when the current temperature in their chosen location goes below the minimum or above the maximum threshold they've set.

## Features

- Connects to a free weather API to fetch real-time temperatures for a specified location.
- Allows users to set their preferred temperature range (minimum and maximum temperature) and location.
- Sends an alert/notification to the user when the current temperature in their chosen location goes below the minimum or above the maximum threshold they've set.

## Dependencies

- Python 3.x
- uAgent library (provide installation instructions or a link to the library)
- plyer library
- infi.systray library
- python-dotenv library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Temperature-Alert-Agent.git

cd Temperature-Alert-Agent

pip install -r requirements.txt
```

2. Run the script:

```bash
pip install -r requirements.txt
```

## Usage

1.Modify the configuration file to set your preferred temperature range and location:

```
 [Configuration]
 Location = YourLocation
 MinTemperature = 20
 MaxTemperature = 30
```

2.Run the Temperature Alert Agent:

```bash
cd app
python3 app.py
```

## License

This project is licensed under the MIT License.

Feel free to copy and paste this Markdown code into your `README.md` file for the "Temperature Alert Agent" project. Customize it according to your project's specific details and requirements.
