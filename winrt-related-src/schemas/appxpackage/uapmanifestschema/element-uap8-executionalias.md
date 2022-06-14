---
title: uap8:ExecutionAlias
description: The executable of a UWP app to be activated from a command prompt (uap8:ExecutionAlias).
ms.date: 04/21/2020
ms.topic: reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap8:ExecutionAlias
The executable of a UWP app to be activated from a command prompt.

## Element Hierarchy
<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap3-extension-manual.md">&lt;uap3:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap3-appexecutionalias.md">&lt;uap3:AppExecutionAlias&gt;</a></dt>
<dd><b>&lt;uap8:ExecutionAlias&gt;</b></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<uap8:ExecutionAlias Alias             = An executable in the form of a string followed by ".exe".
    uap8:AllowOverride = Boolean value. 
    desktop10:UseDesktopChangeRouter = Boolean value. 
    desktop10:DropTarget = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    desktop10:UseUrl = Boolean value.
    desktop10:EnvironmentPath = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
    desktop10:DropTarget = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    desktop10:UseUrl = Boolean value.
    desktop10:EnvironmentPath = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.
>

    <!-- Child elements -->
    (desktop10:SupportedProtocols)?
    
</uap8:ExecutionAlias>
```

## Attributes and Elements
### Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Alias | The name of the UWP app executable. | An executable in the form of a string followed by ".exe". | Yes |
| uap8:AllowOverride | A value that indicates whether to override the UWP app executable. | Boolean value. | No |
| desktop10:UseDesktopChangeRouter | Used by debugger applications to avoid file dialog deadlocks when debugging the Windows Explorer process. Only supported on extension instances that specify CompatMode="classic". Only supported on desktop SKUs. | Boolean value. | No |
| desktop10:DropTarget | The CLSID of an object, usually a local server rather than an in-process server, that implements [IDropTarget](/windows/win32/api/oleidl/nn-oleidl-idroptarget). By default, when the drop target is an executable file and no value is provided for *DropTarget*, the shell converts the list of dropped files into a command-line parameter and passes it to [ShellExecuteEx](/windows/win32/api/shellapi/nf-shellapi-shellexecuteexw) in the *lpParameters* parameter. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |
| desktop10:UseUrl | Specifies that the application can accept a URL, instead of a file name, on the command line. Applications that can open documents directly from the internet, like web browsers and media players, should set this entry. When **ShellExecuteEx** starts an application and this value is not set to true, **ShellExecuteEx** downloads the document to a local file and invokes the handler on the local copy. | Boolean value. | No |
| desktop10:EnvironmentPath | A string containing a semicolon-delimited list of directories specifying the the fully qualified path to the application executable. The value is appended to the PATH environment variable when an application is launched with a call to **ShellExecuteEx**. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |

## Remarks

The attributes and child elements from the desktop10 namespace are only supported on extension instances that specify CompatMode="classic" and are only supported on desktop SKUs.

## Requirements

| **Namespace** | **Value** |
|---------------|-----------|
| **uap8** | `http://schemas.microsoft.com/appx/manifest/uap/windows10/8` |
| **desktop10** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/10` |


