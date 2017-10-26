---
Description: Provides details for each element, attribute, and data type that defines the schema for the bundle manifest for UWP apps.
Search.Product: eADQiWindows 10XVcnh
title: Bundle manifest schema reference
ms.assetid: 20fba0dd-b7d6-47c8-9d9f-a8831bda627c
author: mcleblanc
ms.author: markl
keywords: windows 10, uwp, schema, bundle manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---

# Bundle manifest schema reference


This reference provides details for each element, attribute, and data type that defines the schema for the bundle manifest for UWP apps. The schema definition file is BundleManifestSchema.xsd.

The following table lists all of the elements in this schema, sorted alphabetically by name.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Bundle](element-bundle.md)</td>
<td><p>Defines the root element of a bundle manifest. The manifest describes the structure and capabilities of the software to the system.</p></td>
</tr>
<tr class="even">
<td>[Identity](element-identity.md)</td>
<td><p>Defines a globally unique identifier for a bundle. A bundle identity is represented as a tuple of attributes of the bundle.</p></td>
</tr>
<tr class="odd">
<td>[Package](element-package.md)</td>
<td><p>Defines one of the app packages or resource packages in the bundle.</p></td>
</tr>
<tr class="even">
<td>[Packages](element-packages.md)</td>
<td><p>Defines the app packages and resource packages that are contained in the bundle.</p></td>
</tr>
<tr class="odd">
<td>[Resource](element-resource.md)</td>
<td><p>Declares language, resolution scale, and DirectX feature level for a resource in the package.</p></td>
</tr>
<tr class="even">
<td>[Resources](element-resources.md)</td>
<td><p>Declares languages, resolution scales, and DirectX feature levels for the resources that the package contains.</p></td>
</tr>
</tbody>
</table>

 

 

 



