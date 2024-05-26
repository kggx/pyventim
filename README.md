[![Testing](https://github.com/kggx/pyventim/actions/workflows/testing.yml/badge.svg?branch=main)](https://github.com/kggx/pyventim/actions/workflows/testing.yml)
[![Documentation](https://github.com/kggx/pyventim/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/kggx/pyventim/actions/workflows/docs.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)
[![Python](https://img.shields.io/pypi/pyversions/pyventim?label=Python)](https://pypi.org/project/pyventim/)
[![PyPI Latest Release](https://img.shields.io/pypi/v/pyventim.svg?label=PyPI)](https://pypi.org/project/pyventim/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyventim.svg?label=PyPI%20downloads)](https://pypi.org/project/pyventim/)
[![Coverage](https://codecov.io/github/kggx/pyventim/coverage.svg?branch=main)](https://app.codecov.io/github/kggx/pyventim)

---

> [!NOTE]
> Consider the whole project as unstable until version 1.0.0 is reached.

# pyventim

A Python module to fetch usable data with a reverse engineered Eventim API.

## Description

The [Eventim](https://www.eventim.com/) API has some public endpoints but also hidden data in the HTML responses. The project goal is to provide away to fetch this data with simple to use python objecs.

> [!IMPORTANT]
> Be aware that the APIs of Eventim can change without notice and therefore break the module.

## Getting Started

### Dependencies

- Python >= 3.10
- Requests >= 2.31.0
- lxml >= 5.2.2
- Pydantic >= 2.7.0

### Installing

```bash
pip install pyventim
```

### Quick start

To find attractions we can use the exploration endpoint:

```python
import pyventim

# Create the Eventim class
eventim = pyventim.Eventim()

# Returns an iterator that fetches all pages off the search endpoint.
attractions = eventim.explore_attractions(search_term="Landmvrks")

# We can loop over each attraction. The module handles fetching pages automatically.
for attraction in attractions:
    print(attraction["attractionId"], attraction["name"])
```

Next we use the product group endpoint to fetch events for our attraction and get the events of the html endpoint.

```python

# We loop over each product group and fetch the events automatically.
for product_group in eventim.explore_product_groups(search_term="Landmvrks"):
    product_group_id = product_group["productGroupId"]
    for event in eventim.get_product_group_events_from_calendar(product_group_id):
        print(event["title"], event["eventDate"], event["price"], event["ticketAvailable"], sep=" | ")
```

For a more detailed information please refer to the [documentation](https://kggx.github.io/pyventim/pyventim.html).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Code of conduct

Please follow our [code of conduct](CODE_OF_CONDUCT.md).

## Finding help

The code documentation can be found [here](https://kggx.github.io/pyventim/pyventim.html). However if you encounter a unexpected behaviour: Feel free to open an [issue](https://github.com/kggx/pyventim/issues).

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
