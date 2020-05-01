---

title: desktop4:DesktopIconOverlayHandler
description: Windows Shell icon overlay handlers for cloud based placeholder files. 

ms.date: 4/10/2018
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop4:DesktopIconOverlayHandler

## Description
Windows Shell icon overlay handlers for cloud based placeholder files. 

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
<dt><a href="element-desktop3-cloudfiles.md">&lt;desktop3:CloudFiles&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-desktop4-desktopiconoverlayhandlers.md">&lt;desktop4:DesktopIconOverlayHandlers&gt;</a></dt>
<dd><b>&lt;desktop4:DesktopIconOverlayHandler&gt;</b></dd>
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
<desktop4:DesktopIconOverlayHandler Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Clsid | The class ID of the app that implements the overlay handler. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/4` |