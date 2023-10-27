---
title: desktop7:ApprovedShellExtension
description: Specifies that a shell extension should be added to the approved shell extensions list when installed. 
ms.date: 10/19/2022
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
ms.custom: 19H1
---

# desktop7:ApprovedShellExtension

Specifies that a shell extension should be added to the approved shell extensions list when installed. 

## Element hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<desktop7:Extension\>](element-desktop7-extension.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop7:ApprovedShellExtension\>**

## Syntax

```xml
<desktop7:ApprovedShellExtension
  Name = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.'
  Clsid = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.' />
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Name** | A descriptive name of the Shell extension. This value is not actually used directly by the system but makes it easier to read the entry in the registry. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes |  |
| **Clsid**  | The Clsid of the COM class that implements the Shell Extension.  | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |  |

### Child elements

None.

### Parent elements

| Parent element | Description |
|-|-|
| [Extension](element-desktop6-extension.md) | Defines an extensibility point for the application. |

## Remarks

> [!IMPORTANT]
> Registering an approved shell extension requires that the installer have Administrative permissions, as noted in [Registering Shell Extension Handlers](/windows/win32/shell/reg-shell-exts).
> 
> MSIX apps don't have custom installers, and there's no way for users to manually run them as an Administrator. Instead, MSIX-based apps using the **desktop7:ApprovedShellExtension** element must set the **desktop7:Scope** manifest attribute to the value of *machine* (which will prompt the user to elevate during install). You set the **desktop7:Scope** attribute on the [desktop:Extension](./element-desktop-extension.md) element.
> 
> Equally importantly, to set the **desktop7:Scope** attribute to *machine*, your app's package needs to declare the custom capability `<uap4:CustomCapability Name="Microsoft.classicAppCompatElevated_8wekyb3d8bbwe"/>`. That custom capability is granted to only a limited set of apps.

A shell extension is used in conjunction with a COM class in the manifest that is exposed through Packaged COM (`windows.comServer`; see [com:ComServer](./element-com-comserver.md)). That COM class is used as a [Shell Extension Handler](/windows/win32/shell/handlers) (for example, [DesktopPropertyHandler](./element-desktop2-desktoppropertyhandler.md), [ThumbnailHandler](./element-desktop2-thumbnailhandler.md)). That info applies to all of the shell extensions that you can declare in the app package manifest.

As mentioned in [Registering Shell Extension Handlers](/windows/win32/shell/reg-shell-exts), the impact of including or not including the **desktop7:ApprovedShellExtension** element is whether or not the shell extension would be turned off when an administrator on the machine turns on the key **EnforceShellExtensionSecurity**.

## Requirements

| Item  | Value  |
|--|--|
| Namespace | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/7` |
| **Minimum OS Version** | Windows 10 (Build 19645) |
