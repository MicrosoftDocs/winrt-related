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
  uap10:Parameters = 'An optional string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

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
| **uap10:HostId** | This value specifies the app ID of the host app for the extension. | An alphanumeric string with a value between 1 and 255 characters in length. Must begin with a letter. |
| **uap10:Parameters** | Contains command line parameters for the extension. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [Certificates](element-certificates.md) | Declares a package extensibility point of type **windows.certificates**. The app requires one or more certificates from the specified certificate stores. |
| [InProcessServer](element-inprocessserver.md) | Declares a package extensibility point of type **windows.activatableClass.inProcessServer**. The app uses a dynamic link library (`.dll`) that exposes one or more activatable classes. |
| [OutOfProcessServer](element-outofprocessserver.md) | Declares a package extension point of type **windows.activatableClass.outOfProcessServer**. The app uses an executable (`.exe`) that exposes one or more activatable classes. |
| [ProxyStub](element-proxystub.md) | Declares a package extensibility point of type **windows.activatableClass.proxyStub**. A proxy can be composed of one or more interfaces. |
| [PublisherCacheFolders](element-publishercachefolders.md) | Declares a package extensibility point of type **windows.publisherCacheFolders**. This specifies one or more folders that the package shares with other packages from the same publisher. |
| [com:ComInterface](element-com-package-interface.md) | Declares a package extension point of type **windows.comInterface**. |
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
