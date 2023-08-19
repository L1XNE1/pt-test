{ pkgs ? import <nixpkgs> {}, ... }:
pkgs.mkShell {
  name = "python-shell";
  packages = with pkgs; [
    (let
      python-pkgs = p: with p; [ requests setuptools ];
    in pkgs.python3.withPackages python-pkgs)
  ];
}




### Это временное окружение собранное на ОС NixOS со всеми зависимостями для этого проекта
