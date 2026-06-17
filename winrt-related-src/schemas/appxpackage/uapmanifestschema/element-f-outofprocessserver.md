---
title: OutOfProcessServer
description: Declares a package extension point of type windows.activatableClass.outOfProcessServer (Windows 10).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, package manifest
no-loc: [Package, Extensions, Package, Extensions, Extension, OutOfProcessServer]
---

# OutOfProcessServer

Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-package-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extension>`](element-f-package-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<OutOfProcessServer>`**  

## Syntax

```xml
<Package
  xmlns="http://schemas.microsoft.com/appx/manifest/foundation/windows10">
  ...
  <OutOfProcessServer
    ServerName = 'A required alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character.'
    uap5:RunFullTrust = 'An optional boolean value.'
    uap5:IdentityType = 'An optional string that can have one of the following values: "activateAsPackage", or "activateAsActivator".' >

    <!-- Child elements -->
    Path
    Arguments?
    Instancing
    ActivatableClass{1,65535}

  </OutOfProcessServer>
</Package>
```

### Key

`?` optional (zero or one)
`{}` specific range of occurrences

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ServerName** | Any syntactically valid string that's unique within the package. By convention, it's the name of the executable. | A alphanumeric string between 1 and 255 characters in length. Must begin with an alphabetic character. | Yes |  |
| **uap5:RunFullTrust** | If true, the server will be launched with a Windows Desktop Bridge token, as opposed to a UWP token. | An optional boolean value. | No |  |
| **uap5:IdentityType** | The activation type of the server. | An optional string that can have one of the following values: *activateAsPackage*, *activateAsActivator*. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [Path](element-f-outofprocessserver-path.md) | The path to the executable. |
| [Arguments](element-f-arguments.md) | Specifies the list of comma-separated arguments to pass to the executable. |
| [Instancing](element-f-instancing.md) | Specifies whether the executable runs as a single instance or can run as multiple instances. |
| [ActivatableClass](element-f-outofprocessserver-activatableclass.md) | Declares a runtime class associated with the extensibility point. |

## Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-f-package-extension.md) | Declares an extensibility point for the package. |

## Requirements


| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **uap5** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/5` |
| **Minimum OS Version** | <!-- TODO: Add minimum OS version --> |


## Remarks

If the `IdentityType` is set to `activateAsPackage`, the server will be launched with a token that doesn't vary based on the activating process's token.

## Examples

```xml
<Extension
  Category="windows.activatableClass.outOfProcessServer">
  <OutOfProcessServer
    ServerName="Microsoft.SDKSamples.ToastServer">
    <Path>Microsoft.Samples.ExeServerAuthoring.exe</Path>
    <Instancing>singleInstance</Instancing>
    <ActivatableClass
      ActivatableClassId="Microsoft.Samples.ExeServerAuthoring.Toaster" />
  </OutOfProcessServer>
</Extension>
```
