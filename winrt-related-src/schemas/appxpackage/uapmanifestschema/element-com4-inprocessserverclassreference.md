---
title: com4:InProcessServerClassReference
description: TBD
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:InProcessServerClassReference



## Description
TBD



## Element Hierarchy
<dl><dt><a href = "element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl><dt><a href = "element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl><dt><a href = "element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl><dt><a href = "element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl><dt><a href = "element-com4-surrogateserver.md">&lt;com4:SurrogateServer&gt;</a></dt>
<dd>
<b>&lt;com4:InProcessServerClassReference&gt;</b>
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
<com4:InProcessServerClassReference     EnableOleDefaultHandler = Boolean.
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
></com4:InProcessServerClassReference>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| EnableOleDefaultHandler | This should be set to true if the default value of the [InprocHandler32](/windows/win32/com/inprochandler32) key is "Ole32.dll". Otherwise it should be omitted. The default value is false. | Boolean.| Yes |
| Id | The Id attribute corresponds to the CLSID (HKCR\CLSID\{MyGuid}). | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
