---

title: desktop3:Content
description: Defines the content information of an AutoPlayHandler.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:Content
Defines the content information of an AutoPlayHandler.


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
<dt><a href="element-desktop3-extension.md">&lt;desktop3:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop3-AutoPlayHandler.md">&lt;desktop3:AutoPlayHandler&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop3-invokeaction.md">&lt;desktop3:InvokeAction&gt;</a></dt>
<dd><b>&lt;desktop3:Content&gt;</b></dd>
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
</dd>
</dl>


## Syntax
```syntax
<desktop3:Content ContentEvent       = A string between 1 and 255 characters in length. Backward slashes ('\') are not allowed.
                  Verb               = A string between 1 and 64 characters in length that consists of alphanumeric, period, dash, and space characters only.
                  DropTargetHandler? = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
                  Parameters?        = A string between 1 and 256 characters in length. />
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ContentEvent | The name of a content event raised when a volume device such as a camera memory card, USB drive, or DVD is inserted into the PC. | A string between 1 and 255 characters in length. Backward slashes ('\') are not allowed. | Yes |
| Verb | A literal value, specifying the action. Possible values can include (but aren't limited to): Show, play, import, and open. | A string between 1 and 64 characters in length that consists of alphanumeric, period, dash, and space characters only. | Yes |
| DropTargetHandler | A GUID that identifies the class ID of the app that implements the [IDropTarget](/dotnet/api/microsoft.visualstudio.ole.interop.idroptarget?view=visualstudiosdk-2017) interface. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | No |
| Parameters | Parameters provided to start your app if the [IDropTarget](/dotnet/api/microsoft.visualstudio.ole.interop.idroptarget?view=visualstudiosdk-2017) interface is not implemented. | A string between 1 and 256 characters in length. | No |

## Requirements

|               |      Value                                                       |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |