import os

def lighthouse(url, output=None):
	output_path = "lighthouse.report.html"
	if output:
		output_path = output + "_" + output_path

	os.popen(f"lighthouse --view --quiet \
				--no-update-notifier --no-enable-error-reporting \
				--output=html --output-path={output_path} \
				{url}")
