package com.framework.selenium.api.base;

import java.io.File;
import java.time.Duration;

import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

public class DriverInstance  {

	private static final ThreadLocal<RemoteWebDriver> remoteWebdriver = new ThreadLocal<RemoteWebDriver>();
	private static final ThreadLocal<WebDriverWait> wait = new  ThreadLocal<WebDriverWait>();

	public void setWait() {
		wait.set(new WebDriverWait(getDriver(),Duration.ofSeconds(30)));
	}

	public WebDriverWait getWait() {
		return wait.get();
	}

	public void setDriver(String browser, boolean headless) {		
		switch (browser) {
		case "chrome":
			ChromeOptions options = new ChromeOptions();
			options.addArguments("--start-maximized"); 
			options.addArguments("--disable-notifications"); 
			options.addArguments("--incognito");
			options.addArguments("--remote-allow-origins=*");
			remoteWebdriver.set(new ChromeDriver(options));
			break;
		case "firefox":
		     FirefoxOptions option = new FirefoxOptions();
		     option.addArguments("--start-maximized");
		     option.addArguments("--disable-notifications");
		     option.addArguments("--incognito");
		     option.addArguments("--remote-allow-origins=*");
		     remoteWebdriver.set(new FirefoxDriver(option));
			break;
		case "edge":
		     EdgeOptions option1 = new EdgeOptions();
		     option1.addArguments("--start-maximized");
		     option1.addArguments("--disable-notifications");
		     //option1.addArguments("--incognito");
		     remoteWebdriver.set(new EdgeDriver(option1));
			break;
		case "ie":
			remoteWebdriver.set(new InternetExplorerDriver());
		default:
			break;
		}
	}
	public RemoteWebDriver getDriver() {
		return remoteWebdriver.get();
	}
	
}
