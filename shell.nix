let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = [
    # Python 3.12 + packages
    (pkgs.python312.withPackages (python-pkgs: [
      python-pkgs.requests
      python-pkgs.pytest
      python-pkgs.black
      python-pkgs.pdoc
    ]))
  ];
}
