---
title: com4:ClassReference (in SurrogateServer)
description: TBD
ms.date: 03/13/2022
ms.topic: reference
keywords: windows 10, windows 11, uwp, schema, manifest, com
---

# com4:ClassReference (in SurrogateServer)



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
<b>&lt;com4:ClassReference&gt;</b>
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
<com4:ClassReference     Path = A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", |, ?, or *.
    ThreadingModel = "Both" | "STA" | "MTA" | "MainSTA" | "Neutral"
    EnableOleDefaultHandler = Boolean.
    Id = A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
></com4:ClassReference>
```


## Attributes

| Attribute | Description | Data type | Required |
| -----------| -------------| -----------| ----------|
| Path | TBD | One of the following values: A string between 1 and 256 characters in length that cannot contain these characters: <, >, :, ", ,, ?, or *.| Yes |
| ThreadingModel | TBD | One of the following values: "Both" , "STA" , "MTA" , "MainSTA" , "Neutral"| Yes |
| EnableOleDefaultHandler | TBD | Boolean.| Yes |
| Id | TBD | A GUID in the form xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.| Yes |



## Requirements
| Prefix | Value |
| ---------------| -------------------------------------------------------------|
| com4 | http://schemas.microsoft.com/appx/manifest/com/windows10/4 |
