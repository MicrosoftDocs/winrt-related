---
author: mcleanbyron
title: desktop3:CloudFiles
description: Registration for the handlers implemented in an application and context menu options for cloud based placeholder files.
ms.author: mcleans
ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:CloudFiles

## Description
Registration for the handlers implemented in an application and context menu options for cloud based placeholder files. 

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
<dd><b>&lt;desktop3:CloudFiles&gt;</b></dd>
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
<desktop3:CloudFiles IconResource = A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: <, >, :, %, ", |, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both. >
    
  <!-- Child elements -->
  ( desktop3:CustomStateHandler,
    desktop3:ThumbnailProviderHandler, 
    desktop3:ExtendedPropertyHandler,
    desktop3:BannersHandler,
    desktop3:CloudFilesContextMenus,
    desktop4:ContentUriSource )
    
</desktop3:CloudFiles>
```

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| IconResource | A path to an icon that represents the sync provider. | A string between 1 and 256 characters in length that ends with ".jpg", ".png", or ".jpeg" that can't contain these characters: &lt;, &gt;, :, %, ", &#124;, ?, or *. In this string, the / and \ characters can't be the first or last characters. Also, the string can contain / or \ but not both. | Yes |

## Child Elements

| Child Element | Description |
|---------------|-------------|
| [desktop3:CustomStateHandler](element-desktop3-customstatehandler.md) | Registration of a Windows Shell CustomStateHandler for cloud based placeholder files. |  
| [desktop3:ThumbnailProviderHandler](element-desktop3-ThumbnailProviderHandler.md) | Registration of a Windows Shell ThumbnailProviderHandler for cloud based placeholder files. |  
| [desktop3:ExtendedPropertyHandler](element-desktop3-ExtendedPropertyHandler.md) | Registration of a Windows Shell ExtendedPropertyHandler for cloud based placeholder files. |  
| [desktop3:BannersHandler](element-desktop3-BannersHandler.md) | Registration of a Windows Shell BannersHandler for cloud based placeholder files. |  
| [desktop3:CloudFilesContextMenus](element-desktop3-CloudFilesContextMenus.md) | Registration of a context menu for a cloud based placeholder file. |
| [desktop4:ContentUriSource](element-desktop4-contenturisource.md) | Registration of a Windows Shell ContentUriSource enabling cloud storage providers to provide a file ID for a given local path. |  

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