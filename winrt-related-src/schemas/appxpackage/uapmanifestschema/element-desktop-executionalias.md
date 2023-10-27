---
title: desktop:ExecutionAlias
description: The executable of a UWP app to be activated from a command prompt (desktop:ExecutionAlias).
ms.date: 04/21/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop:ExecutionAlias

The executable of a UWP app to be activated from a command prompt.

## Element Hierarchy

[\<Package\>](element-package.md)

&nbsp;&nbsp;&nbsp;&nbsp;[\<Applications\>](element-applications.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Application\>](element-application.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<Extensions\>](element-1-extensions.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;[\<uap3:Extensions\>](element-uap3-extension-manual.md)

&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;**\<desktop:ExecutionAlias\>**

## Syntax

```xml
<desktop:ExecutionAlias
    Alias = 'An executable in the form of a string followed by ".exe".'
    uap8:AllowOverride = 'A boolean value.'
    desktop10:UseDesktopChangeRouter = 'A boolean value.' 
    desktop10:DropTarget = 'A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
    desktop10:UseUrl = 'A boolean value.'
    desktop10:EnvironmentPath = 'A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

    <!-- Child elements -->
    desktop10:SupportedProtocols

</desktop:ExecutionAlias>
```

## Attributes and elements

### Attributes

| Attribute | Description | Data type | Required | Default value | Default value |
|-|-|-|-|-|
| **Alias** | The name of the UWP app executable. | An executable in the form of a string followed by `.exe`. | Yes |  |
| **uap8:AllowOverride** | A value that indicates whether to override the UWP app executable. | A boolean value. | No |  |
| **desktop10:UseDesktopChangeRouter** | Used by debugger applications to avoid file dialog deadlocks when debugging the Windows Explorer process. | A boolean value. | No |  |
| **desktop10:DropTarget** | The CLSID of an object, usually a local server rather than an in-process server, that implements [IDropTarget](/windows/win32/api/oleidl/nn-oleidl-idroptarget). By default, when the drop target is an executable file and no value is provided for *DropTarget*, the shell converts the list of dropped files into a command-line parameter and passes it to [ShellExecuteEx](/windows/win32/api/shellapi/nf-shellapi-shellexecuteexw) in the *lpParameters* parameter. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **desktop10:UseUrl** |If set to true, specifies that the application can accept a URL, instead of a file name, on the command line. Applications that can open documents directly from the internet, like web browsers and media players, should use this value. When **ShellExecuteEx** starts an application and this value is set to false, the default behavior, **ShellExecuteEx** downloads the document to a local file and invokes the handler on the local copy. | A boolean value. | No |  |
| **desktop10:EnvironmentPath** | A string containing a semicolon-delimited list of directories specifying the the fully qualified path to the application executable. The value is appended to the PATH environment variable when an application is launched with a call to **ShellExecuteEx**. | A string with a value between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

### Child elements

| Child element | Description |
|-|-|
| [desktop10:SupportedProtocols](element-desktop10-supportedprotocols.md) | Specifies the supported URL protocol schemes for a given key. |

### Parent elements

| Parent element | Description |
|-|-|
| [uap3:Extension](element-uap3-extension-manual.md) | Declares an extensibility point for the app. |

## Remarks

The attributes and child elements from the desktop10 namespace are only supported on extension instances that specify CompatMode="classic" and are only supported on desktop SKUs.

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/foundation/windows10` |
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |
