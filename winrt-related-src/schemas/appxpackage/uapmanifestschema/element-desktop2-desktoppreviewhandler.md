---
author: laurenhughes
ms.assetid: 7095e2f1-6781-4961-b436-1192c55fa53f
title: desktop2:DesktopPreviewHandler
description: Enables declaration of a preview handler for a file type association.
ms.author: lahugh
ms.date: 04/05/2017
ms.topic: reference
ms.prod: windows
ms.technology: winrt-reference
keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop2:DesktopPreviewHandler


## Description
Enables declaration of a preview handler for a file type association.

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
<dd><b>&lt;desktop2:DesktopPreviewHandler&gt;</b></dd>
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
<desktop2:DesktopPreviewHandler Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
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
Note that the Clsid attribute from PreviewHandler **must** match the ID attribute under the Class element in the [SurrogateServer](element-com-surrogateserver.md) element from the COM registration in the app manifest.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/2</p></td>
</tr>
</tbody>
</table>