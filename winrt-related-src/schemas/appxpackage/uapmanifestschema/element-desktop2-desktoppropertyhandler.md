---

ms.assetid: 97d6c3ae-db3f-46c8-b7b0-418bd30bcbdd
title: desktop2:DesktopPropertyHandler
description: Enables declaration of a property handler for a file type association.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:DesktopPropertyHandler


## Description
Enables declaration of a property handler for a file type association.

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
<dt><a href="element-uap-extension.md">&lt;uap:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-uap-filetypeassociation.md">&lt;uap:FileTypeAssociation&gt;</a></dt>
<dd><b>&lt;desktop2:DesktopPropertyHandler&gt;</b></dd>
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
<desktop2:DesktopPropertyHandler Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
                                 ManualSafeSave? = Boolean.
                                 EnableShareDenyNone? = Boolean.
                                 EnableShareDenyWrite? = Boolean.
                                 NoOplock? = Boolean. >   
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Clsid | The ID of the class in the app's package. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |
| ManualSafeSave | Sets STGM_TRANSACTED (true = off). | Boolean. | No |
| EnableShareDenyNone | Sets STGM_SHARE_DENY_NONE. | Boolean. | No |
| EnableShareDenyWrite | Sets STGM_SHARE_DENY_WRITE. | Boolean. | No |
| NoOplock | Disables oplock logic. This is used to close the file if another process attempts to access the file. | Boolean. | No |

## Remarks
Note that the Clsid attribute from PropertyHandler **must** match the ID attribute under the Class element in the [SurrogateServer](element-com-surrogateserver.md) element from the COM registration in the app manifest.

## Requirements

|               |                                                             |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/2` |