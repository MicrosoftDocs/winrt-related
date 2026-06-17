---
title: desktop:ExecutionAlias
description: The executable of a UWP app to be activated from a command prompt (desktop:ExecutionAlias).
ms.date: 06/05/2026
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension
no-loc: [Package, Applications, Application, Extensions, desktop:Extension, desktop:AppExecutionAlias, desktop:ExecutionAlias]
---

# desktop:ExecutionAlias

The executable of a UWP app to be activated from a command prompt.

## Element hierarchy

**[`<Package>`](element-f-package.md)**  
&nbsp;&nbsp;&nbsp;└─ [`<Applications>`](element-f-applications.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Application>`](element-f-application.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<Extensions>`](element-f-application-extensions.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ [`<desktop:Extension>`](element-desktop-extension.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop:AppExecutionAlias>`**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ **`<desktop:ExecutionAlias>`**

## Syntax

```xml
<desktop:ExecutionAlias
  Alias = 'A required string between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: <, >, :, ", /, \, &#124;, ?, or *.'
  uap8:AllowOverride = 'An optional boolean value.'
  desktop10:UseDesktopChangeRouter = 'An optional boolean value.'
  desktop10:DropTarget = 'An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.'
  desktop10:UseUrl = 'An optional boolean value.'
  desktop10:EnvironmentPath = 'An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.' >

  <!-- Child elements -->
  desktop:SupportedProtocols?

</desktop:ExecutionAlias>
```

### Key

`?` optional (zero or one)

## Attributes

| Attribute | Description | Data type | Required | Default value |
|-|-|-|-|-|
| **Alias** |  The name of the UWP app executable.  | A string between 1 and 256 characters in length that must end with `.exe` and cannot contain these characters: <, >, :, ", /, \, &#124;, ?, or *. | Yes |  |
| **uap8:AllowOverride** |  A value that indicates whether to override the UWP app executable.  | An optional boolean value. | No |  |
| **desktop10:UseDesktopChangeRouter** |  Used by debugger applications to avoid file dialog deadlocks when debugging the Windows Explorer process.  | An optional boolean value. | No |  |
| **desktop10:DropTarget** |  The CLSID of an object, usually a local server rather than an in-process server, that implements [IDropTarget](/windows/win32/api/oleidl/nn-oleidl-idroptarget). By default, when the drop target is an executable file and no value is provided for *DropTarget*, the shell converts the list of dropped files into a command-line parameter and passes it to [ShellExecuteEx](/windows/win32/api/shellapi/nf-shellapi-shellexecuteexw) in the *lpParameters* parameter.  | An optional GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |  |
| **desktop10:UseUrl** |  If set to true, specifies that the application can accept a URL, instead of a file name, on the command line. Applications that can open documents directly from the internet, like web browsers and media players, should use this value. When **ShellExecuteEx** starts an application and this value is set to false, the default behavior, **ShellExecuteEx** downloads the document to a local file and invokes the handler on the local copy.  | An optional boolean value. | No |  |
| **desktop10:EnvironmentPath** |  A string containing a semicolon-delimited list of directories specifying the the fully qualified path to the application executable. The value is appended to the PATH environment variable when an application is launched with a call to **ShellExecuteEx**.  | An optional string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |  |

## Child elements

| Child element | Description |
|-|-|
| [desktop10:SupportedProtocols](element-desktop10-supportedprotocols.md) | Specifies the supported URL protocol schemes for the extension. |

## Parent elements

| Parent element | Description |
|-|-|
| [uap3:AppExecutionAlias](element-uap3-appexecutionalias.md) | Specifies the application's execution alias to determine the executable of the app to be activated. |

## Requirements

| Item | Value |
|--|--|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10` |
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| **Minimum OS Version** | Windows 10 version 1607 (Build 14393) |

## Remarks

The attributes and child elements from the desktop10 namespace are only supported on extension instances that specify CompatMode="classic" and are only supported on desktop SKUs.

## Examples

<!-- Author content goes here -->
