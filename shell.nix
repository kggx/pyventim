let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = [
    # Python 3.12 + packages
    (pkgs.python312.withPackages (python-pkgs: [
      python-pkgs.requests
      python-pkgs.black
      python-pkgs.pdoc
      python-pkgs.twine
      python-pkgs.build
      python-pkgs.pytest
      python-pkgs.pytest-cov
      python-pkgs.flake8
      python-pkgs.lxml
      python-pkgs.pydantic
    ]))
  ];
}
