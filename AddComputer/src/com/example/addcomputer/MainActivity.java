package com.example.addcomputer;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends Activity {
	Button btn_plus=null;
	EditText jiashu=null,beijiashu=null;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		btn_plus=(Button)findViewById(R.id.btn_plus);
		jiashu=(EditText)findViewById(R.id.txt_jiashu);
		beijiashu=(EditText)findViewById(R.id.txt_beijiashu);
		btn_plus.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View arg0) {
				Intent intent=new Intent();
				intent.setClass(MainActivity.this, OtherActivity.class);
				Bundle bundle=new Bundle();
				int result=Integer.valueOf(jiashu.getText().toString())+Integer.valueOf(beijiashu.getText().toString());
				bundle.putString("result",result+"");
				intent.putExtras(bundle);
				startActivity(intent);
				finish();
			}
		});
	}
}
