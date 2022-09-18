---
description: Declares a package extension point of type windows.activatableClass.outOfProcessServer (Windows 10).
Search.Product: eADQiWindows 10XVcnh
title: OutOfProcessServer (Windows 10)
ms.assetid: 575ad44f-e0e3-4682-a082-8d8184bd8dd4
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/05/2017
---

# OutOfProcessServer (Windows 10)

Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extension\>](element-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<OutOfProcessServer\>**

## Syntax

```xml
<OutOfProcessServer
  ServerName = 'An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.' 
  RunFullTrust = 'An optional boolean value.'
  IdentityType = 'An optional string that can be one of the following values: "activateAsPackage" or "activateAsActivator".' >

  <!-- Child elements -->
  Path
  Arguments?
  Instancing
  ActivatableClass{1,65535}

</OutOfProcessServer>
```

### Key

`?`   optional (zero or one)
`{}`   specific range of occurrences

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **ServerName** | The name of the executable. | An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | Yes |  |
| **RunFullTrust** | If true, the server will be launched with a Windows Desktop Bridge token, as opposed to a UWP token. | An optional boolean value. | No |  |
| **IdentityType** | The activation type of the server. | An optional string that can be one of the following values: *activateAsPackage* or *activateAsActivator*. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [ActivatableClass (type: CT_OutOfProcessActivatableClass)](element-1-activatableclass.md) | Declares a runtime class associated with the extensibility point. |
| [Arguments](element-arguments.md) | Specifies the list of comma-separated arguments to pass to the executable. |
| [Instancing](element-instancing.md) | Specifies whether the executable runs as a single instance or can run as multiple instances. |
| [Path (type: ST_Executable)](element-1-path.md) | The path to the executable. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extension (in type: CT_PackageExtensions)](element-extension.md) | Declares an extensibility point for the package. |

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

## Requirements

|   | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
