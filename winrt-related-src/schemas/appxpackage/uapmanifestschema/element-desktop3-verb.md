---

title: desktop3:Verb
description: Specifies the names of items in the File Explorer context menu for cloud based placeholder files.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:Verb

## Description
Specifies the names of items in the File Explorer context menu for cloud based placeholder files.

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
<dt><a href="element-desktop3-cloudfilescontextmenus.md">&lt;desktop3:CloudFilesContextMenus&gt;</a></dt>
<dd><b>&lt;desktop3:Verb&gt;</b></dd>
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
<desktop3:Verb Id    = An alphanumeric string from 3 to 64 characters in length.
               Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The name that appears in the File Explorer context menu.  | An alphanumeric string from 3 to 64 characters in length. | Yes |
| Clsid | The class ID of the app that implements the context menu. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/desktop/windows10/3</p></td>
</tr>
</tbody>
</table>