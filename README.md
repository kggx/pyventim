[![Testing](https://github.com/kggx/pyventim/actions/workflows/testing.yml/badge.svg?branch=main)](https://github.com/kggx/pyventim/actions/workflows/testing.yml)
[![Documentation](https://github.com/kggx/pyventim/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/kggx/pyventim/actions/workflows/docs.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

---

# pyventim

A Python module to fetch usable data with a reverse engineered Eventim API.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

- Python >= 3.10
- Requests >= 2.31.0

### Installing

```bash
pip install pyventim
```

### Quick start

#### Public API

```python
# Import the module
from pyventim.public import EventimExploration

# We are testing against a long running german musical prone NOT to change
search_for = "Stage Theater im Hafen Hamburg"
sort_by = "DateAsc"

# Returns attractions found by the explorer api given the search term.
explorer: EventimExploration = EventimExploration()
result = explorer.explore_attractions(
    search_term=search_for,
    sort=sort_by,
)
```

For a more detailed information please read the [documentation]().

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Code of conduct

Please follow our [code of conduct](CODE_OF_CONDUCT.md).

## Finding help

The code documentation can be found [here](). However if you encounter a unexpected behaviour: Feel free to open an [issue](https://github.com/kggx/pyventim/issues).

## Contributing

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

If youre looking to work on the pyventim codebase:

1. Fork the repository.
1. Make your changes and follow common code practices as well as Python PEP standards.
1. Open a merge request and follow the instructions.
1. Be awesome!

For bug reports: Please head over to the [issues page](https://github.com/kggx/pyventim/issues).

As contributors and maintainers to this project, you are expected to abide by pyeventim' code of conduct. More information can be found at: [Contributor Code of Conduct](CODE_OF_CONDUCT.md)

### Thank you!

Thank you for contributing to this project!

<a href="https://github.com/kggx/pyventim/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kggx/pyventim"/>
</a>

## Maintainers

\*Preferred method of contact.

- Kilian Braun ([\*DeltaChat](https://i.delta.chat/#97C62CBA0454D4E4FFA475DEA0177351147E5B3E&a=tyzcvpuoz%40nine.testrun.org&n=Kilian&i=isE8C2JZ1IA&s=-_KJ9JqJdSt) | [Email](mailto:hello@kilianbraun.de?subject=PYVENTIM%3A%20General%20question%20about%20the%20project))

## Acknowledgments

- [awesome-readme](https://github.com/matiassingers/awesome-readme) is a simple readme template!
- [Open source checklist](https://dev.to/zt4ff_1/setting-up-your-github-repository-for-open-source-development-43ce) is good guide to follow if going open source!
- [Contributor Covenant](https://www.contributor-covenant.org) have an awesome code of conduct!
- [DeltaChat](https://delta.chat/) is a great and simple privacy focused messanger app via email!
