package info.sweetduet.ksnctf.jewel;

import android.app.Activity;
import android.app.AlertDialog.Builder;
import android.content.res.Resources;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;
import java.io.InputStream;
import java.math.BigInteger;
import java.security.Key;
import java.security.MessageDigest;
import java.security.spec.AlgorithmParameterSpec;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class JewelActivity extends Activity
{
  public void onCreate(Bundle paramBundle)
  {
    super.onCreate(paramBundle);
    setContentView(2130903040);
    // 端末の国際移動体装置識別番号(IMEI;International Mobile Equipment Identifier)を取得
    Object localObject1 = ((TelephonyManager)getSystemService("phone")).getDeviceId();
    try
    {
      paramBundle = MessageDigest.getInstance("SHA-256");
      paramBundle.update(((String)localObject1).getBytes("ASCII"));
      paramBundle = new BigInteger(paramBundle.digest()).toString(16);
      if (!((String)localObject1).substring(0, 8).equals("99999991"))
      {
        new AlertDialog.Builder(this).setMessage("Your device is not supported").setCancelable(false).setPositiveButton("OK", new b(this)).show();
        return;
      }
      if (!paramBundle.equals("356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5"))
      {
        new AlertDialog.Builder(this).setMessage("You are not a valid user").setCancelable(false).setPositiveButton("OK", new a(this)).show();
        return;
      }
    }
    catch (Exception paramBundle)
    {
      Toast.makeText(this, paramBundle.toString(), 1).show();
      return;
    }
    Object localObject2 = getResources().openRawResource(2130968576);
    paramBundle = new byte[((InputStream)localObject2).available()];
    ((InputStream)localObject2).read(paramBundle);
    localObject1 = new SecretKeySpec(("!" + (String)localObject1).getBytes("ASCII"), "AES");
    localObject2 = new IvParameterSpec("kLwC29iMc4nRMuE5".getBytes());
    Cipher localCipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
    localCipher.init(2, (Key)localObject1, (AlgorithmParameterSpec)localObject2);
    paramBundle = localCipher.doFinal(paramBundle);
    localObject1 = new ImageView(this);
    ((ImageView)localObject1).setImageBitmap(BitmapFactory.decodeByteArray(paramBundle, 0, paramBundle.length));
    setContentView((View)localObject1);
  }
}

/* Location:           /home/yyy/ctf/ksnctf/Jewel/
 * Qualified Name:     info.sweetduet.ksnctf.jewel.JewelActivity
 * JD-Core Version:    0.6.2
 */
