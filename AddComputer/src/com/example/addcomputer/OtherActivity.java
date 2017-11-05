package com.example.addcomputer;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

public class OtherActivity extends Activity{
	Button bt=null;
	
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_other);
		bt=(Button)findViewById(R.id.returnToMain);
		bt.setOnClickListener(new ButtonClickListener());
		Intent intent=this.getIntent();
		Bundle bundle=intent.getExtras();
		String results=bundle.getString("result");
		EditText tv=(EditText)findViewById(R.id.txt_result);
		System.out.println("1");
		tv.setText(results);
		System.out.println("2");
		
	}
	class ButtonClickListener implements OnClickListener {
		@Override
		public void onClick(View arg0) {
			Intent intent=new Intent();
			intent.setClass(OtherActivity.this, MainActivity.class);
			OtherActivity.this.startActivity(intent);
			OtherActivity.this.finish();
		}
	}

}
