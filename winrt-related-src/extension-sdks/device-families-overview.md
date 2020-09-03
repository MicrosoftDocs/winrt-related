---
title: Programming with extension SDKs
description: An explanation of device families, extension SDKs, and API contracts, and how to program with them.
ms.topic: reference
ms.date: 09/02/2020
keywords: windows 10, uwp, device family, extension sdk, api contract
---

# Programming with extension SDKs

In order to understand how Windows 10 allows your Universal Windows Platform (UWP) app to most effectively target different classes of devices, this topic explains the following concepts.

- Device family
- Extension SDK
- API contract

We also show how to use them in your programming.

## Video&mdash;Introduction to UWP and device families
&nbsp;
<iframe src="https://channel9.msdn.com/Blogs/One-Dev-Minute/Introduction-to-UWP-and-Device-Families/player" width="640" height="360" allowFullScreen frameBorder="0"></iframe>

## Device families, and your app's target device family

A device family identifies the APIs, system characteristics, and behaviors that you can expect across a class of devices.

![device families](images/device-family-tree.png)

A device family is the foundation of an operating system (OS). For example, PCs and tablets run a desktop edition of the OS, and that's based on the Desktop device family. IoT devices run an IoT edition of the OS, which is based on the IoT device family.

Each child device family adds its own APIs to the APIs that it inherits from the Universal device family. The resulting union of APIs in a child device family is guaranteed to be present in an OS that's based on that device family, and therefore on every device running that OS.

The decision about which device family your app will *target* is yours to make. And that decision impacts your app in these important ways. It determines

- the families of devices on which your app can be installed from the Microsoft Store (and consequently the form factors that you need to consider when you design your app's UI), and
- the particular set of APIs that you can rely on being present on a device running your app (the host device).

By *rely on being present*, we mean that you can call those APIs without needing to test to see whether they're present on the host device. The device family that you target provides that guarantee (different guarantees for different device families).

By default, your UWP app targets the Universal device family. And that means that your app can be installed on *all* Windows 10 devices, and that you can rely on a large core set of APIs being present on the host device. An app like that needs to have a highly adaptive UI, and comprehensive input capabilities, because it can run on a wide variety of devices. 

Alternatively, you could choose to target a different device family&mdash;for example, the Desktop device family, or the IoT device family. As a result, there'd be fewer devices that could host your app, but you'd be able to rely on a larger set of APIs being present on those devices (the set in the Universal device family, plus the set in the target device family). An app like that typically need be only moderately adaptive; it can be somewhat specialized in its UI and input capabilities, because it can run on only a specific kind of device.

But it's better, if you can, to have the best of both worlds. We'll see how to achieve that in the next section.

## Extension SDKs, and how to reference them

If in your Visual Studio project you change your target from the Universal device family to some other device family, then you need to add a reference to the extension SDK corresponding to that device family. That makes the APIs in that device family available to your project.

If you target the Desktop device family, then add a reference to the **Windows Desktop Extensions for the UWP** extension SDK. If you target the IoT device family, then add a reference to the **Windows IoT Extensions for the UWP** extension SDK.

![Select the IoT extension SDK](images/SelectIoTExtensionSDK.png)

There are also **Windows Mobile Extensions for the UWP**, and **Windows Team Extensions for the UWP**.

If you target the Universal device family, then you can still add a reference to one or more extension SDKs. Reference whichever extension SDKs contain the additional APIs that you'd like to call. Remember, you're targeting the Universal device family, so those are the only APIs that you can *rely on*  being present. For APIs in the extension SDK(s) you referenced, you'll need to test that they're present on the host device at run time before you call them (more details in the [Writing code](#writing-code) section below). Of course, you don't need to perform that test for APIs in the Universal device family. The is the best-of-both-worlds scenario that we mentioned in the previous section.

By using an extension SDK, you can target the unique APIs of a specific family of devices, and thereby access their specialized capabilities. You can do that whether you target the corresponding device family or not.

## Choose a device family to target

Here are some considerations to help you decide which device family to target.

### Maximize your app's reach

To reach the maximum range of kinds of devices with your app, and consequently to have it run on as many devices as possible, your app will target the Universal device family. Specifically, you'll target a range of versions of the Universal device family.

The **TargetDeviceFamily** element in your app package manifest source file (the `Package.appxmanifest` file) has attributes named **MinVersion** and **MaxVersionTested**. For more info about how to target a range of versions, and examples, see [**TargetDeviceFamily**](/uwp/schemas/appxpackage/uapmanifestschema/element-targetdevicefamily).

### Limit your app to one kind of device

You may not want your app to run on a wide range of devices; perhaps it's specialized for a desktop PC, or for an Xbox console. In that case, you can choose to target one of the child device families.

### Limit your app to a subset of all possible devices

Instead of targeting the Universal device family, or targeting one of the child device families, you can instead target two (or more) child device families. Targeting Desktop and Mobile might make sense for your app. Or Desktop and Team. Or Desktop, Mobile, and Team, and so on.

### Exclude support for a particular version of a device family

In rare cases, you might want your app to run everywhere *except* on devices with a particular version of a particular device family. For example, let's say that your app targets version 10.0.x.0 of the universal device family. When the operating system version changes in the future&mdash;say to 10.0.x.2&mdash;at that point, you can specify that your app runs everywhere except version 10.0.x.1 of Xbox by targeting your app to 10.0.x.0 of Universal and 10.0.x.2 of Xbox. Your app will then be unavailable to the set of device family versions within Xbox 10.0.x.1 (inclusive) and earlier.

By default, Microsoft Visual Studio specifies **Windows.Universal** as the target device family in the app package manifest file. To specify the device family or device families that your app is offered to from within the Store, manually configure the [**TargetDeviceFamily**](/uwp/schemas/appxpackage/uapmanifestschema/element-targetdevicefamily) element in your Package.appxmanifest file.

## Tooling

By default, you'll probably want to target the broadest possible device family. When you're ready to see how your app looks and lays out on a particular device, use the device preview toolbar in Visual Studio to preview your UI on a small or medium mobile device, on a PC, or on a large TV screen. That way you can tailor and test your adaptive visual states:

![visual studio 2015 device preview toolbar](images/vs2015-device-preview-toolbar.png)

You don't have to make a decision in advance about every device type that you'll support. You can add an additional device size to your project later.

## Writing code

Much of your code will be universal in the sense that it will run the same way on every device. But for code tailored to particular device families, you'll have the option to use adaptive code. Let's consider these different cases.

### Call an API that's implemented by your target device family

Whenever you want to call an API in a UWP app, you'll want to know whether or not the API is implemented by the device family that your app is targeting. Visual Studio IntelliSense shows you only the APIs that are available for the extension SDKs that you've chosen. If you haven't selected an extension SDK, then you'll see only the APIs available to the Universal device family.

The API documentation also tells you which device family an API is part of. If you look at the **Requirements** section, then you'll see what the implementing device family is, and which version of that device family the API appears in.

### Call an API that's not implemented by your target device family

There'll be cases when you want to call an API in an extension SDK that you've referenced, but that API is not part of the device family that you're targeting. For example, you might be targeting the Universal device family, but have a Desktop API which&mdash;provided that the app happens to be running on a desktop device&mdash;you'd like to call. In that case, you can opt to write adaptive code in order to call that API.

### Write adaptive code by using **ApiInformation**

There are two steps to writing adaptive code. The first step is to make the APIs that you want to access available to your project. To do that, add a reference to the extension SDK that represents the device family that owns the APIs that you want to conditionally call.

The second step is to use the [**ApiInformation**](/uwp/api/windows.foundation.metadata.apiinformation) class in a condition in your code to test for the presence of the API that you want to call. This condition is evaluated wherever your app runs, but it evaluates to `true` only on devices where the API is present and therefore available to call.

If you want to call just a small number of APIs, then you could use the [**ApiInformation.IsTypePresent**](/uwp/api/Windows.Foundation.Metadata.ApiInformation) method like this.

```csharp
// Note: Cache the value instead of querying it more than once.
bool isHardwareButtonsAPIPresent =
    Windows.Foundation.Metadata.ApiInformation.IsTypePresent("Windows.Phone.UI.Input.HardwareButtons");

if (isHardwareButtonsAPIPresent)
{
    Windows.Phone.UI.Input.HardwareButtons.CameraPressed += HardwareButtons_CameraPressed;
}
```

In this case, there's confidence that the presence of the [**HardwareButtons**](/uwp/api/Windows.Phone.UI.Input.HardwareButtons) class implies the presence of the [**CameraPressed**](/uwp/api/Windows.Phone.UI.Input.HardwareButtons) event, because the class and the member have the same requirements info. But in time, new members will be added to already-introduced classes, and those members will have later "introduced in" version numbers. In such cases, instead of using **IsTypePresent**, you can test for the presence of individual members by using **IsEventPresent**, **IsMethodPresent**, **IsPropertyPresent**, and similar methods. Here's an example.

```csharp
bool isHardwareButtons_CameraPressedAPIPresent =
    Windows.Foundation.Metadata.ApiInformation.IsEventPresent
        ("Windows.Phone.UI.Input.HardwareButtons", "CameraPressed");
```

The set of APIs within a device family is further broken down into subdivisions known as API contracts. You can use the **ApiInformation.IsApiContractPresent** method to test for the presence of an API contract. This is useful if you want to test for the presence of a large number of APIs that all exist in the same version of an API contract.

```csharp
bool isWindows_Devices_Scanners_ScannerDeviceContract_1_0Present =
    Windows.Foundation.Metadata.ApiInformation.IsApiContractPresent
        ("Windows.Devices.Scanners.ScannerDeviceContract", 1, 0);
```

## See also

* [Device family extension SDKs and API contracts](/uwp/extension-sdks/)
* [What's a Universal Windows Platform (UWP) app](/windows/uwp/get-started/universal-application-platform-guide)
* [Version-adaptive apps](/windows/uwp/debug-test-perf/version-adaptive-apps)
