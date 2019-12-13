---

title: desktop3:ThumbnailProviderHandler
description: Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. 

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:ThumbnailProviderHandler

## Description
Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. 

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
<dd><b>&lt;desktop3:ThumbnailProviderHandler&gt;</b></dd>
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
<desktop3:ThumbnailProviderHandler Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. />
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Clsid | The class ID of the app that implements the ThumbnailProviderHandler, used for thumbnail images of placeholder files. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. | Yes |

## See also
[Creating Shell Extension Handlers](https://msdn.microsoft.com/library/windows/desktop/cc144067(v=vs.85).aspx)

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