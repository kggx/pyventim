let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    # MITM Proxy to reverse engineer apis
    pkgs.mitmproxy
    pkgs.mitmproxy2swagger

    # Python 3.12 + packages
    (pkgs.python312.withPackages (python-pkgs: [
      python-pkgs.requests

    ]))
  ];
}