# *antares-xpansion* CMake Build Instructions

 [CMake version](#cmake-version) | [Dependencies](#dependencies) | [Building](#building-antares-solution) |
 
## [CMake version](#cmake-version)
CMake 3.x must be used. 

You can download latest Windows version directly from [CMake website](https://cmake.org/download/).

## [Python version](#python-version)
Python 3.x must be used.

You can download latest Windows version directly from [Python website](https://www.python.org/downloads/windows/).

Required python modules can be installed with :
```
pip install -r src/src_python/requirements.txt
pip install -r src/src_python/tests/examples/requirements.txt
```

## [Dependencies](#deps)
*antares-xpansion* depends on several mandatory libraries. 
 - [JsonCpp](https://github.com/open-source-parsers/jsoncpp)
 - [Google Test](https://github.com/google/googletest)
 - [OR-Tools](https://github.com/AntaresSimulatorTeam/or-tools/tree/rte_dev_sirius)
 - Boost : mpi serialization (Only for MPI benders compilation)
 - [Doxygen](https://www.doxygen.nl/index.html) for documentation generation
 - [GraphViz](https://graphviz.org/) for doxygen use

This section describes the install procedures for the third-party Open source libraries used by *antares-xpansion*.
The install procedure can be done
- by compiling the sources after cloning the official git repository
- by using VCPKG

### VCPKG

For Windows we will use [vcpkg](https://github.com/microsoft/vcpkg) to download and compile the librairies.

You must install the corresponding [vcpkg-triplet](https://vcpkg.readthedocs.io/en/latest/users/integration/#triplet-selection) depending on Antares version and libraries load:

- ``x64-windows``        : 64 bits version with dynamic librairies load
- ``x86-windows``        : 32 bits version with dynamic librairies load
- ``x64-windows-static`` : 64 bits version with static librairies load
- ``x86-windows-static`` : 32 bits version with static librairies load

The vcpkg-triplet used will be named [vcpg-triplet] later in this document.

#### 1 Install vcpkg 

vcpkg can be installed anywhere on your computer :

```
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
.\bootstrap-vcpkg.bat
```

Note :
> all vcpkg command further described must be run from vcpkg folder. This folder will be named [vcpkg_root] later in this document.


#### 2 Install dependencies
```
cd [vcpkg_root]
vcpkg install jsoncpp:[vcpg-triplet] 
vcpkg install gtest:[vcpg-triplet] 
vcpkg install boost-mpi:[vcpg-triplet]
vcpkg install openssl:[vcpg-triplet] 
vcpkg install curl:[vcpg-triplet]
```

Note :
> On Windows, boost-mpi compilation depends on MSMPI redistributable package. Please follow VCPKG procedure :
> ```
> Please install the MSMPI redistributable package before trying to install this port.
>     The appropriate installer has been downloaded to:
>      [vcpkg_root]/downloads/msmpisetup-10.0.12498.exe
> ``` 

### Automatic librairies compilation from git
[Antares dependencies compilation repository](https://github.com/AntaresSimulatorTeam/antares-deps) is used as a git submodule for automatic librairies compilation from git.

ALL dependency can be built at configure time using the option `-DBUILD_ALL=ON` (`OFF` by default). For a list of available option see [Antares dependencies compilation repository](https://github.com/AntaresSimulatorTeam/antares-deps).

Some dependencies can't be installed with a package manager. They can be built at configure step with a cmake option  : `-DBUILD_not_system=ON` (`OFF` by default):
```
cmake -B _build -S . -DCMAKE_BUILD_TYPE=Release -DUSE_SEQUENTIAL=true -DUSE_MPI=true -DBUILD_not_system=ON -DDEPS_INSTALL_DIR=<deps_install_dir>
```

**Warning :**
> boost-mpi is not compiled with this repository. VCPKG use is mandatory or you must compile boost-mpi by yourself.

#### Defining dependency install directory
When using multiple directories for antares development with multiple branches it can be useful to have a common dependency install directory.

Dependency install directory can be specified with `DEPS_INSTALL_DIR`. By default install directory is `<antares_xpansion_checkout_dir>/../rte-antares-deps-<build_type>`

Note :
> `DEPS_INSTALL_DIR` is added to `CMAKE_PREFIX_PATH`

## [antares-solver build](antares-solver-build)
*antares-xpansion* needs the *antares-solver* binary in order to execute the whole simulation process. A Cmake option allows compilation of *antares-solver* at configure : `-DBUILD_antares_solver=ON` (default `ON`)

## [Building *antares-xpansion*](#build)
- Update git submodule for dependency build :
```
git submodule update --init antares-deps
```
- Configure build with cmake

```
cmake -B _build -S . -DCMAKE_TOOLCHAIN_FILE=[vcpkg_root]/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=[vcpkg-triplet] -DCMAKE_BUILD_TYPE=Release -DUSE_SEQUENTIAL=true -DUSE_MPI=true
```

- Build
 ```
cmake --build _build --config Release -j8
```
Note :
> Compilation can be done on several processor with ```-j``` option.

## [Installer creation](#installer)
CPack can be used to create the installer after the build phase :
 ```
cd _build
cpack -G ZIP
```