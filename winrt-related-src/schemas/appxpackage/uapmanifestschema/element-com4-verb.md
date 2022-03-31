---
title: com4:Verb
description: The verb to be registered for an application. (com4:Verb)
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:Verb



## Description
The verb to be registered for an application.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-class.md">&lt;com4:Class&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-verbs.md">&lt;com4:Verbs&gt;</a></dt>
<dd>
<b>&lt;com4:Verb&gt;</b>
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
<com4:Verb     Id = An integer between -6 and 1000.
    DisplayName = A string between 1 and 256 characters in length. This string is localizable.
    AppendMenuFlag = An integer between 0 and 2431.
    OleVerbFlag = An integer between 0 and 3.
></com4:Verb>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Id | The Id number of the verb. Verbs are numbered consecutively. | An integer between -6 and 1000.| Yes |
| DisplayName | Describes how the verb is appended by [AppendMenu](/windows/win32/api/winuser/nf-winuser-appendmenua). | A string between 1 and 256 characters in length. This string is localizable.| Yes |
| AppendMenuFlag | Indicates how the verb should appear in the menu. | An integer between 0 and 2431.| Yes |
| OleVerbFlag | Describes the attributes of a verb. Use either 0 or a value from the [OLEVERBATTRIB](/windows/win32/api/oleidl/ne-oleidl-oleverbattrib) enumeration. | An integer between 0 and 3.| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
