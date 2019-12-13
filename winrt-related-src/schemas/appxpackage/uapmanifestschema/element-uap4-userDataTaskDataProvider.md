---

ms.assetid: b7722b81-6aae-4dc2-97a5-e7f729e10f25
title: uap4:UserDataTaskDataProvider
description: Enables an app to become a DataProvider for a task.

ms.date: 04/05/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, desktop, extension 
---

# uap4:UserDataTaskDataProvider

## Description
Enables an app to become a DataProvider for a task.

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
<dt><a href="element-uap4-extension.md">&lt;uap4:Extension&gt;</a></dt>
<dd><b>&lt;uap4:UserDataTaskDataProvider&gt;</b></dd>
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
<uap4:UserDataTaskDataProvider ServerName? = A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. >
```

### Key
`?` optional (zero or one)

## Attributes
| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| ServerName | The server that will be used to satisfy the contract activation. This is only used for PPLE host processes. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | No |

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/uap/windows10/4</p></td>
</tr>
</tbody>
</table>