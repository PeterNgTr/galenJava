package tests;

/**
 * Created by thanhnguyen on 1/26/17.
 */

import components.GalenTestBase;
import org.testng.annotations.Test;
import java.io.IOException;

public class WelcomePageTest extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void welcomePage_shouldLookGood_onDevice(TestDevice device) throws IOException {
        load("/");
        checkLayout("/specs/welcomePage.spec", device.getTags());
    }

}