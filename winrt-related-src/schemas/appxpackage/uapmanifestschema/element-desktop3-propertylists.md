---

title: desktop3:PropertyLists
description: Contains a list of properties to show under the properties tab of a file.

ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# desktop3:PropertyLists


## Description
Contains a list of properties to show under the properties tab of a file.

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
<dd><b>&lt;desktop3:PropertyLists&gt;</b></dd>
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
<desktop3:PropertyLists>
  <!-- Child elements -->
  desktop3:PropertyList
</desktop3:PropertyLists>   
```


## Child Elements
| Child Element | Description |
|---------------|-------------|
| [PropertyList](element-desktop3-propertylist.md) | Defines properties shown under the properties tab of a file. |

## See Also
[Using Property Lists](/windows/win32/properties/building-property-handlers-property-lists)


## Requirements

|               |       Value                                                      |
|---------------|-------------------------------------------------------------|
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/desktop/windows10/3` |