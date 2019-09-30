---
author: mcleanbyron
title: uap5:AppExecutionAlias
description: Specifies the application's execution alias to determine the executable of the app to be activated.
ms.author: mcleans
ms.date: 10/10/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap5:AppExecutionAlias

## Description
Specifies the application's execution alias to determine the executable of the app to be activated.

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
<dt><a href="element-uap5-extension.md">&lt;uap5:Extension&gt;</a></dt>
<dd><b>&lt;uap5:AppExecutionAlias&gt;</b></dd>
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
<uap5:AppExecutionAlias desktop4:Subsystem? = String value. Can be one of the following: "console", "windows" >   
    uap5:ExecutionAlias{0,1000}
</uap5:AppExecutionAlias>
```

### Key
`{}`   specific range of occurrences


## Attributes and Elements
### Attributes
## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| desktop4:Subsystem | Indicates whether the app is a standard UWP app or a UWP console app. | String value. Can be one of the following: "console", "windows" | No |

### Child Elements
| Child Element | Description |
|---------------|-------------|
| [ExecutionAlias](element-uap5-ExecutionAlias.md) | The executable of a UWP app to be activated from a command prompt. |


## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/5</p></td>
</tr>
</tbody>
</table>