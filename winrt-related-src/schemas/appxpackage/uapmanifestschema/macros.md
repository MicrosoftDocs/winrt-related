---
title: Macros in the package manifest schema
description: You can use macros in the values of some attributes in the package manifest schema.
keywords: windows 11, windows 10, uwp, schema, package manifest, macros
ms.topic: reference
ms.date: 04/26/2024
---

# Macros in the package manifest schema

A macro is a dynamically-evaluated manifested value. You can use macros in the values of some attributes in the package manifest schema. Examples of such attributes are [uap11:CurrentDirectoryPath](/uwp/schemas/appxpackage/uapmanifestschema/element-application#attributes) and **uap11:Parameters**.

## Syntax

A macro is expressed in the form `$(macro_name)`.

* That syntax expands to the value in the *Expands to* column below.
* For a single `$` character in an attribute value, use the escape sequence `$$`.

| Macro name | Expands to |
| - | - |
|env:environmentvariable|GetEnvironmentVariable(environmentvariable)|
|package.currentDirectoryPath|GetCurrentDirectory()|
|package.effectiveExternalPath|GetPackagePathByFullName2(...PackagePathType_EffectiveExternal...)|
|package.effectivePath|GetPackagePathByFullName2(...PackagePathType_Effective...)|
|package.installedPath|GetPackagePathByFullName2(...PackagePathType_Install...)|
|package.machineExternalPath|GetPackagePathByFullName2(...PackagePathType_MachineExternal...)|
|package.mutablePath|GetPackagePathByFullName2(...PackagePathType_Mutable...)|
|package.userExternalPath|GetPackagePathByFullName2(...PackagePathType_UserExternal...)|
|system.path|GetSystemDirectory()|
|windows.path|GetWindowsDirectory()|

## An example scenario

In this hypothetical example scenario, I've created a packaged app (written in Python) named `MyPackagedPythonApp.py`. To run it, I need the following in my manifest:

`<Application...Executable="python.exe" uap10:TrustLevel="mediumIL" uap10:RuntimeBehavior="packagedClassicApp" uap10:Parameters="-m MyPackagedPythonApp.py --default=1">`

That configuration causes this command to execute:

`"C:\Program Files\WindowsApps\MyApp_1.2.3.4_x64__1234567890abc\python.exe" -m MyPackagedPythonApp.py --default=1`

But that command fails if the current folder doesn't happen to be `C:\Program Files\WindowsApps\MyApp_1.2.3.4_x64__1234567890abc`.

So I might try to to specify my `.py` file by absolute filename, like this:

`"C:\Program Files\WindowsApps\MyApp_1.2.3.4_x64__1234567890abc\python.exe" -m "C:\Program Files\WindowsApps\MyApp_1.2.3.4_x64__1234567890abc\MyPackagedPythonApp.py" --default=1`

But I, as the developer, don't know whether the package *will* be installed to that path. Perhaps the user's drive was full, so the package ended up on drive Q. And the path changes every time I bump my package version. So this is where macros come to the rescue.

I specify my `.py` file by using a macro for the path (which will be evaluated at runtime) to the package's location, like this:

`<Application...Executable="python.exe" uap10:TrustLevel="mediumIL" uap10:RuntimeBehavior="packagedClassicApp" uap10:Parameters="-m $(package.effectivePath)\MyPackagedPythonApp.py --defcon=1">`

Now, at runtime, the command is executed as I expect. But Windows has dynamically filled in the right path (again, at runtime), like this:

`"C:\Program Files\WindowsApps\MyApp_1.2.3.4_x64__1234567890abc\python.exe" -m "C:\Program Files\WindowsApps\MyApp_1.2.3.4_x64__1234567890abc\MyPackagedPythonApp.py" --default=1`
