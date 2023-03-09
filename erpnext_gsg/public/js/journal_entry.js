frappe.ui.form.on('Journal Entry', {
	setup: function(frm) {
	//	alert("Journal Entry Test");
	set_field_options("voucher_type", ["Journal Entry","Cash Entry","Credit Card Entry","Debit Note","Credit Note",
	"Contra Entry","Excise Entry","Write Off Entry","Opening Entry","Depreciation Entry","Exchange Rate Revaluation","Exchange Gain Or Loss",
	"Deferred Revenue","Deferred Expense"])

	}
});

//frm.set_df_property(frm.doc.voucher_type == "Inter Company Journal Entry", "hidden",true);
