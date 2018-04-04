---
Description: Identifies the device family that your package targets. 
Search.Product: eADQiWindows 10XVcnh
title: TargetDeviceFamily (Windows 10)
ms.assetid: 457745aa-bc12-427b-b1f1-74c1618753c0
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
ms.prod: windows
ms.technology: winrt-reference
ms.topic: reference
ms.date: 04/05/2017
---
# TargetDeviceFamily (Windows 10)

Identifies the device family that your package targets. For more info about device families, see [Device families overview](https://docs.microsoft.com/uwp/extension-sdks/device-families-overview).

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-dependencies.md">&lt;Dependencies&gt;</a></dt>
<dd><b>&lt;TargetDeviceFamily&gt;</b></dd>
</dl>
</dd>
</dl>

## Syntax

``` syntax
<TargetDeviceFamily Name             = An alphanumeric string. May contain period and dash characters.
                    MinVersion       = A version string in quad notation, "Major.Minor.Build.Revision".
                    MaxVersionTested = A version string in quad notation, "Major.Minor.Build.Revision". />
```

## Attributes and Elements

### Attributes

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
<th>Data type</th>
<th>Required</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>MaxVersionTested</strong></td>
<td><p>The maximum version of the device family that your app is targeting that you have tested it against. This is used at runtime to determine the effective process space for quirks.</p></td>
<td>A version string in quad notation, &quot;Major.Minor.Build.Revision&quot;.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td><strong>MinVersion</strong></td>
<td><p>The minimum version of the device family that your app is targeting. Used for applicability at deployment time. If the device family version of the system is lower than MinVersion, then the app is not considered applicable.</p></td>
<td>A version string in quad notation, &quot;Major.Minor.Build.Revision&quot;.</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Name</strong></td>
<td><p>The name of the device family that your app is targeting. See the Remarks section for more information.</p></td>
<td>An alphanumeric string. May contain period and dash characters.</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

### Child Elements

None.

### Parent Elements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Dependencies](element-dependencies.md)</td>
<td><p>Declares other packages that a package depends on to complete its software.</p></td>
</tr>
</tbody>
</table>

## Examples

To target the set of APIs known as the "universal device family" (which means your app runs on all devices), just specify that one device family, as in the example below. You can still write adaptive code to light up APIs outside of the universal device family when your app is running on devices in specific device families. Versions 10.0.x.0 and 10.0.y.0 can, of course, be the same value.

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.Universal" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
</Dependencies>
```

**Note**  If you target "Windows.Universal" with both "MinVersion" and "MaxVersionTested" set to version 10.0.0.0, your app will use the versions specified in the Target Min Version and Target Version of the project file, respectively. If you are using "Windows.Universal" with "MinVersion" and "MaxVersionTested" set to a value other than 10.0.0.0, the app will target the specified "MinVersion" and "MaxVersionTested" instead of the values specified in the project file.

All child device families "derive" from (that is, they include) the "universal device family" set of APIs. So, a child device family implies "universal plus other child-device-family-specific APIs". When you target a child device family, you don't need to mention universal. In this next example, the app is targeting the set of APIs known as the "mobile device family", and consequently it will run only on devices that implement the mobile device family set of APIs (mobile devices). Replace "Mobile" with "Desktop", "Xbox", "Holographic", "IoT", or "IoTHeadless" for example, if you want to target another device family.

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.Mobile" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
</Dependencies>
```

**Note**  If the app is targeting a device family other than "Windows.Universal", the "MinVersion" and "MaxVersionTested" must be properly specified for the device family that is targeted.

To target the Xbox device family, set the Name attribute to "Windows.Xbox". Note that to target the Xbox device family, the MinVersion must be set to at least 10.0.14393.0.

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.Xbox" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
</Dependencies>
```

If your app is created specifically for HoloLens and is not supported on other platforms, specify the target device family "Windows.Holographic".

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.Holographic" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
</Dependencies>
```

If your app targets the Windows 10 Team Edition exclusively, set the Name attribute to "Windows.Team". This is commonly used for Microsoft Surface Hub devices.

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.Team" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
</Dependencies>
```

If you want to target the IoT Core platform, set the Name attribute to "Windows.IoT". For a headless IoT app, use "Windows.IoTHeadless".

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.IoT" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
</Dependencies>
```

**Note**  Currently, apps targeting IoT or IoTHeadless are not valid in the app store and should be used for development purposes only.

In this example, the app targets the mobile and desktop device families. Consequently the app can run on mobile devices or on desktop devices, but no others. Note that the app must use adaptive code to call any API that is not in the universal device family set of APIs (unless the API happens to be shared by both device families).

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.Mobile" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
    <TargetDeviceFamily Name="Windows.Desktop" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
</Dependencies>
```

In this last example, the app targets the universal device family (so, by default, it runs on all devices with the specified minimum version). The exception being that, for devices that implement the mobile device family, the app requires at least version 10.0.m.0 to be present. This is how you indicate that you do not support versions of child device families earlier than a specified minimum version, even if that differs from the version you support for the general case (the universal device family case). Also note the MaxVersionTested value for the mobile device family dependency in the example. Where z &gt; n, the app will run on version 10.0.z.0 of a mobile device, but it will experience 10.0.n.0-version behavior from the platform on that version.

```XML
<Dependencies>
    <TargetDeviceFamily Name="Windows.Universal" MinVersion="10.0.x.0" MaxVersionTested="10.0.y.0"/>
    <TargetDeviceFamily Name="Windows.Mobile" MinVersion="10.0.m.0" MaxVersionTested="10.0.n.0"/>
</Dependencies>
```

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://schemas.microsoft.com/appx/manifest/foundation/windows10</p></td>
</tr>
</tbody>
</table>