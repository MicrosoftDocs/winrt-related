---
author: mcleanbyron
ms.assetid: a7b26419-0322-4269-928b-01634fc8c255
title: com:Verb
description: The verb to be registered for an application.
ms.author: mcleans
ms.date: 03/29/2017
ms.topic: reference


keywords: windows 10, uwp, schema, manifest, com
---


# com:Verb

## Description
The verb to be registered for an application.

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
<dt><a href="element-com-extension.md">&lt;com:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-comserver.md">&lt;com:ComServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogateserver.md">&lt;com:SurrogateServer&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogateserver-class.md">&lt;com:Class&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-com-surrogate-verbs.md">&lt;com:Verbs&gt;</a></dt>
<dd><b>&lt;com:Verb&gt;</b></dd>
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
</dd>
</dl>
</dd>
</dl>


## Syntax
```syntax
<com:Verb
    Id = An integer value in the range of -6 to 1000.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
    AppendMenuFlag = An integer value in the range of 0 to 2431.
    OleVerbFlag = An integer value in the range of 0 to 3. >
</com:Verb>
```

## Key

## Attributes 

| Attribute | Description | Data type | Required |
|-----------|-------------|-----------|----------|
| Id | The Id number of the verb. Verbs are numbered consecutively. | An integer value in the range of -6 to 1000. | Yes |
| DisplayName | Describes how the verb is appended by [AppendMenu](https://msdn.microsoft.com/library/windows/desktop/ms647616.aspx). | A string between 1 and 256 characters in length. This string is localizable. | Yes |
| AppendMenuFlag | Indicates how the verb should appear in the menu. | An integer value in the range of 0 to 2431. | Yes |
| OleVerbFlag | Describes the attributes of a verb. Use either 0 or a value from the [OLEVERBATTRIB](https://msdn.microsoft.com/library/windows/desktop/ms686659.aspx) enumeration. | An integer value in the range of 0 to 3. | Yes |

## Remarks

## Examples

## Requirements
<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/com/windows10</p></td>
</tr>
</tbody>
</table>