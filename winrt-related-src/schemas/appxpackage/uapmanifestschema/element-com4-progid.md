---
title: com4:ProgId
description: A programmatic identifier (ProgID) that can be associated with a CLSID (com4:ProgId).
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ProgId



## Description
A programmatic identifier (ProgID) that can be associated with a CLSID. The ProgID identifies a class but with less precision than a CLSID because it is not guaranteed to be globally unique.



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dd><b>&lt;com4:ProgId&gt;</b></dd></dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax
```syntax
<com4:ProgId     Id = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
    Clsid = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
    CurrentVersion  = An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1
></com4:ProgId>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Id | The ID of the ProgID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |
| Clsid | Associates a ProgID with a CLSID. | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |
| CurrentVersion  | The version of the ProgID. | An alphanumeric string separated by a period between 1 and 255 characters in length, e.g. Foo.Bar or Foo.Bar.1| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
