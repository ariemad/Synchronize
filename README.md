

<h1 style="text-align: center;">Synchronize</h1>
<p style="text-align: center;">A CLI tool tool that synchronizes two folders: Source and Replica.</p>

[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pytest](https://github.com/ariemad/Synchronize/actions/workflows/pytest.yml/badge.svg)](https://github.com/ariemad/Veeam-Test-Task/actions/workflows/pytest.yml)

## Usage

### ```validate``` Command

Validates the config file.

Informs the user if there is any incorrect value.

```bash
python synchronize validate
```
### ```start``` Command

Runs the synchronization script.

```bash
python synchronize start [--repeat] [--print]
```

- ```--repeat``` - Runs the synchronization tool periodically, according to time interval

- ```--print``` - Prints the logs to the terminal

### ```set``` Command

Changes a value in the config.

```bash
python synchronize set [--option1 value1] [--optionN valueN]
```

- ```--source some/path``` - Defines the source path

- ```--replica some/path``` - Defines the replica path

- ```--log some/path``` - Defines the log path

- ```--interval 12345``` - Defines the synchronization interval in seconds (minimum of 10 seconds)

### ```showlog``` Command

```bash
python synchronize showlog
```

Shows logs.

### ```showconfig``` Command

```bash
python synchronize showconfig
```

Shows config.

## Contributing

PRs accepted.

Please contact me if you wish to contribute.

## License

MIT © Daniel Bray
