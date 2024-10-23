---
description: Declares an extensibility point for the package (in Package/Extensions).
Search.Product: eADQiWindows 10XVcnh
title: Extension (in Package/Extensions) (Windows 10)
ms.assetid: 72f0d1ae-15a4-4eba-a3ca-990f4de2b697
keywords: windows 10, uwp, schema, package manifest
ms.topic: reference
ms.date: 04/10/2018
---

# Extension (in Package/Extensions) (Windows 10)

Declares an extensibility point for the package.

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<Extension\>**

## Syntax

```xml
<Extension
  Category = 'A string that can have one of the following values: "windows.activatableClass.inProcessServer", "windows.activatableClass.outOfProcessServer", "windows.activatableClass.proxyStub", "windows.certificates", "windows.publisherCacheFolders", "windows.comInterface", or "windows.loaderSearchPathOverride".'
  uap10:TrustLevel = 'An optional string that can have one of the following values: "appContainer" or "mediumIL".'
  uap10:RuntimeBehavior = 'An optional string that can have one of the following values: "windowsApp", "packagedClassicApp", or "win32App".'
  uap10:HostId = 'An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap10:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' 
  uap11:Id = 'An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end.'
  uap11:Subsystem = 'An optional string that can have one of the following values: "console" or "windows".'
  uap11:SupportsMultipleInstances = 'An optional boolean value.'
  uap11:ResourceGroup = 'An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter.'
  uap11:CurrentDirectoryPath = 'An optional string that cannot contain these characters: <, >, |, ?, or *. >'
  uap11:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  desktop7:CompatMode = 'An optional string the can have one of the following values: "classic" or "modern".'
  desktop7:Scope = 'An optional string that can have one of the following values: "machine" or "user".'>

  <!-- Child elements -->
  InProcessServer
  OutOfProcessServer
  ProxyStub
  Certificates
  PublisherCacheFolders
  com:ComInterface
  uap6:LoaderSearchPathOverride

</Extension>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Category** | The type of package extensibility point. | A string that can have one of the following values: *windows.activatableClass.inProcessServer*, *windows.activatableClass.outOfProcessServer*, *windows.activatableClass.proxyStub*, *windows.certificates*, *windows.publisherCacheFolders*, *windows.comInterface*, or *windows.loaderSearchPathOverride* | Yes |  |
| **uap10:TrustLevel** | Specifies the trust level of the extension. | An optional string that can have one of the following values: *appContainer* or *mediumIL*. | No |  |
| **uap10:RuntimeBehavior** | Specifies the run time behavior of the extension. | An optional string that can have one of the following values: *windowsApp*, *packagedClassicApp*, or *win32App*. | No |  |
| **uap10:HostId** | This value Specifies the ID of the host runtime for the extension. | An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. |
| **uap10:Parameters** | Contains command line parameters for the extension. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Id** | An identifier for the extension. The ID must be unique for all extensions in a package.| An optional string with a value between 1 and 255 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **uap11:Subsystem** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored.  | An optional string that can have one of the following values: *console* or *windows*. | No |  |
| **uap11:SupportsMultipleInstances** | Specifies whether instances should run in different processes. The default value is false. | An optional boolean value. | No |  |
| **uap11:ResourceGroup** | A tag that you can use to group extension activations together for resource management purposes (for example, CPU and memory). The value you can set ResourceGroup is free-form and flexible. See [Application@ResourceGroup](element-application.md).  | An optional alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. | No |  |
| **uap11:CurrentDirectoryPath** | Specifies the initial directory when the application process is launched. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string that cannot contain these characters: `<`, `>`, `|`, `?`, or `*`. > | No |  |
| **uap11:Parameters** | This attribute is inherited from the base extension syntax and is not applicable to the com4 extension. Other than syntactic validation, this value is ignored. This attribute supports macros. For more info, see [Macros in the package manifest schema](./macros.md). | An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |
| **desktop7:CompatMode** | Specifies whether this extension's information is registered with Windows in classic ways (e.g. unpackaged apps register types with COM via the registry) or in new more scoped ways. The default value is "modern". CompatMode="classic" requires the *Microsoft.classicAppCompat_8wekyb3d8bbwe* capability. | An optional string the can have one of the following values: *classic* or *modern*. | No |  |
| **desktop7:Scope** | Specifies whether the registrations are only visible to other applications running as a user who has this package registered (user), or whether they are visible to all users and services on the machine (machine). The default value is "user". Scope="machine" requires the *Microsoft.classicAppCompatElevated_8wekyb3d8bbwe* capability. | An optional string that can have one of the following values: *machine* or *user*. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Certificates](element-certificates.md) | Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores. |
| [InProcessServer](element-inprocessserver.md) | Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (`.dll`) that exposes one or more activatable classes. |
| [OutOfProcessServer](element-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes. |
| [ProxyStub](element-proxystub.md) | Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces. |
| [PublisherCacheFolders](element-publishercachefolders.md) | Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher. |
| [com:ComInterface](element-com-interface.md) | Declares a package extension point of type **windows.comInterface**. |
| [uap6:LoaderSearchPathOverride](element-uap6-LoaderSearchPathOverride.md) | Declares a package extension point of type **windows.loaderSearchPathOverride**. |

### Parent elements

| Parent element | Description |
|-|-|
| [Extensions (type: CT_PackageExtensions)](element-extensions.md) | Defines one or more extensibility points for the package. |

## Related elements

The following elements have the same name as this one, but different content or attributes:

- [Extension (global)](element-1-extension.md)

## Remarks

Extensibility points are a mechanism by which a package can add functionality in a manner defined by the operating system. An extensibility point is a location where an app can register to execute code or use resources of the current package. To add functionality for a particular app, use the [Application](element-application.md) child element of the [Applications](element-applications.md) element.

The **windows.certificates** extensibility point can't be declared multiple times in a manifest.

## See also

- [App contracts and extensions](/previous-versions/windows/apps/hh464906(v=win.10))

## Requirements

| Item  | Value  |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **com** | `http://schemas.microsoft.com/appx/manifest/com/windows10` |
| **uap6** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/10` |
